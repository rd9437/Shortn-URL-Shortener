from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    urls = db.relationship('URLMap', backref='owner', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    visit_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

# Ensure tables are created
with app.app_context():
    db.create_all()

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not URLMap.query.filter_by(short_url=short_url).first():
            return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    existing = URLMap.query.filter_by(original_url=original_url).first()
    is_new = False

    if existing:
        short_url = existing.short_url
        visit_count = existing.visit_count
        is_new = False
    else:
        short_url = generate_short_url()
        new_mapping = URLMap(
            original_url=original_url,
            short_url=short_url,
            user_id=current_user.id if current_user.is_authenticated else None
        )
        db.session.add(new_mapping)
        db.session.commit()
        visit_count = 0
        is_new = True

    # Store short_url in session for later association
    session['last_short_url'] = short_url

    return render_template('shorten.html', short_url=short_url, visit_count=visit_count, is_new=is_new)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    mapping = URLMap.query.filter_by(short_url=short_url).first()
    if mapping:
        mapping.visit_count += 1
        db.session.commit()
        return redirect(mapping.original_url)
    else:
        return "URL not found", 404

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return "Username already exists", 400
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        # Assign previously shortened URL (if any) to new user
        if 'last_short_url' in session:
            url = URLMap.query.filter_by(short_url=session['last_short_url']).first()
            if url and url.user_id is None:
                url.user_id = new_user.id
                db.session.commit()
            session.pop('last_short_url', None)

        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)

            # Assign previously shortened URL (if any) to user
            if 'last_short_url' in session:
                url = URLMap.query.filter_by(short_url=session['last_short_url']).first()
                if url and url.user_id is None:
                    url.user_id = user.id
                    db.session.commit()
                session.pop('last_short_url', None)

            return redirect(url_for('dashboard'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    urls = URLMap.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', urls=urls)

@app.route('/analytics/<short_url>')
@login_required
def view_analytics(short_url):
    url = URLMap.query.filter_by(short_url=short_url, user_id=current_user.id).first()
    if not url:
        return "Link not found or unauthorized", 404
    return render_template('analytics.html', url=url)

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    # Delete user's URLs first
    URLMap.query.filter_by(user_id=current_user.id).delete()

    # Delete the user
    db.session.delete(current_user)
    db.session.commit()

    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
