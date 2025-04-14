# URL Shortener Web App

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=for-the-badge)](https://rd9437.pythonanywhere.com/)

---
This is a simple URL shortener web application built using Flask. It allows users to shorten long URLs into shorter, more manageable ones.

## Features

+ Shorten long URLs into short, easy-to-share links.
+ Redirect users to the original long URL when they visit the shortened link.
+ Minimalistic user interface for easy use.

## Setup

To run this web application locally, follow these steps:

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/rd9437/url-shortener.git
   ```
2. Navigate to the project directory:
   ```
   cd url-shortener
   ```
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```
   python app.py
   ```
   Open your web browser and visit http://localhost:5000 to access the web application.


## About the Source Code

### Project Structure

The source code for this project is organized as follows:

+ **app.py**: Contains the main Flask application code, including route definitions and URL handling logic.
+ **templates/**: Directory containing HTML templates used by the Flask application for rendering web pages.
+ **static/**: Directory containing static files such as CSS stylesheets, JavaScript files, and images.
+ **confetti.js**: JavaScript file responsible for triggering the confetti animation on the shorten.html page.
+ **styles.css**: CSS stylesheet defining the styles for the HTML templates.

### Dependencies

+ **Flask**: A micro web framework for Python used to build the web application.
+ **canvas-confetti**: JavaScript library for creating confetti animations.

### How It Works

+ The Flask application (`app.py`) handles incoming HTTP requests and serves HTML templates located in the `templates` directory.
+ When a user submits a URL through the form on the landing page (`index.html`), the Flask application generates a shortened URL and renders the `shorten.html` page with the shortened URL.
+ The confetti animation on the `shorten.html` page is triggered by the `confetti.js` JavaScript file when the page loads.
+ Users can click on the "Shorten Another Link" button to return to the landing page and shorten another URL.

## Support
If you encounter any issues or have questions regarding the Resume Builder, please don't hesitate to reach out to me for assistance.

https://rd9437.pythonanywhere.com/





