import smtplib, ssl
from app import app


def send_email(firstname, lastname, email, subject, message):
    port = 465
    smtp_server = "smtp.gmail.com"
    password = app.config['ADMIN_PASS']
    sender_email = app.config['ADMIN_EMAIL']

    receiver_email = "ana.mayer.int@gmail.com"
    text = f"""\
    User: {firstname} {lastname}

    Email: {email}

    Message:
    -----------------------
    {message}
    -----------------------"""
    message = 'Subject: {}\n\n{}'.format(subject, text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



