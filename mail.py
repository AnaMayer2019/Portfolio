from app import db


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    subject = db.Column(db.String(300), index=True)
    message = db.Column(db.String(1000), index=True)

    def __repr__(self):
        return '<Mailer {} {}, email -> {}>'.format(self.firstname, self.lastname, self.email)
