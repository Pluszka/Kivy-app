import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from email_token import EmailToken
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
emailToken = EmailToken()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pwd = db.Column(db.String(500), nullable=False)

    # def __init__(self, name, email, age, pwd):
    #     self.name = name
    #     self.email = email
    #     self.age = age
    #     self.pwd = pwd

@app.route('/confirm_email/<string:token>')
def confirm(token):
    emailToken.confirm_token(token)

    # new_user = User(
    #     name=,
    # # )
    # db.session.add(new_user)
    # db.session.commit()
    return "<h3>Thanks for confirming your e-mail. Your account is created.</h3>"


if __name__ == '__main__':
    # Two lines below required only once, when creating DB.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
