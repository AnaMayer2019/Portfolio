from flask import Flask
from flask import render_template, request, flash, redirect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from utils import send_email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/experience/')
def experience():
    return render_template('experience.html')


@app.route('/interests/')
def interests():
    return render_template('interests.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        first = request.form.get('firstname')
        last = request.form.get('lastname')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        send_email(first, last, email, subject, message)
        flash("Thank you for your message!", 'info')
        return redirect('/')
    return render_template('contact.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html')
