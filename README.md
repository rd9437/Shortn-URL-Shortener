# 🔗 Shortn — URL Shortener Web App

[🌐 Live Demo »](https://rd9437.pythonanywhere.com/)

**Shortn** is a clean, beginner-friendly URL shortener web app built with **Flask**. It allows users to create and manage short, trackable URLs — with or without an account.

---

## ✨ Features

- 🔗 Instantly shorten long URLs
- 📥 Redirect users to the original link when a short URL is visited
- 📈 Track total clicks per URL (logged-in users only)
- 📸 Generate a QR Code for every shortened link
- 📊 View per-link analytics via a personal dashboard
- 👤 Optional user accounts for dashboard access
- ❌ Delete account if you forget your password — no recovery needed
- 🎉 Confetti animation on successful shortening (because why not?)

---

## 🧠 Why Use Shortn?

You **don’t need an account** to shorten links.

However, if you create one, you get:

- A private dashboard with your shortened links
- Click tracking stats
- QR code previews
- The ability to delete your account anytime

---

## 🚀 Getting Started

To run Shortn locally:

### 1. Clone the repository:

```bash
git clone https://github.com/rd9437/url-shortener.git
cd url-shortener
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app:

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🗂️ Project Structure

```
.
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, JS, images)
│   ├── styles.css
│   └── confetti.js
├── templates/            # HTML templates
│   ├── index.html
│   ├── shorten.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   └── analytics.html
└── README.md
```

---

## 🛠️ Tech Stack

- **Flask** — Python web framework
- **Flask-Login** — User authentication
- **Flask-SQLAlchemy** — Database ORM
- **Tailwind CSS** — Modern utility-first CSS
- **canvas-confetti** — Fun confetti animation

---

## 💡 How It Works

- Enter a long URL and get a short, shareable link.
- If you’re logged in, your links are saved to your dashboard.
- Each link has a QR code and click analytics.
- No password recovery: if you forget your password, just delete your account and start fresh.

---

## 🙋 FAQ

**Q: Do I need an account to use Shortn?**  
A: No! Anyone can shorten links. Accounts are only needed for dashboards and analytics.

**Q: Can I reset my password?**  
A: No. For privacy and simplicity, password reset is not available. You can delete your account and create a new one.

**Q: Is my data private?**  
A: Yes. Only you can see your dashboard and links when logged in.

---

## 📬 Support

Have questions or suggestions?  
Open an issue or reach out via [rudransh.tech](https://rudransh.tech).






