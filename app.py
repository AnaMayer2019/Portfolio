from flask import Flask
from flask import render_template, request, flash, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from utils import send_email
from mail import Mail


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
        m = Mail(firstname=first, lastname=last, email=email, subject=subject, message=message)
        db.session.add(m)
        db.session.commit()
        return redirect('/')
    return render_template('contact.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html')


@app.route('/messagelist', methods=['GET', 'POST'])
def message_list():
    if request.method == "POST":
        print('abc')
        if request.form.get('password') == app.config['LOG_PASS']:
            messages = Mail.query.all()
            return render_template('message_list.html', messages=messages)
    return render_template('login.html')
