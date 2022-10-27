import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from email_token import EmailToken

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
    token = db.Column(db.String(500), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)

@app.route('/confirm_email/<string:token>')
def confirm(token):
    emailToken.confirm_token(token)
    return f"<h3>Thanks for confirming your e-mail. Your account is created.</h3>"

@app.route('/<string:pwd>/<string:name>/<string:email>/<int:age>/<string:token>')
def create_user(pwd, name, email, age, token):
    secure_password = generate_password_hash(
        pwd,
        method='pbkdf2:sha256',
        salt_length=8
    )
    new_user = User(
        name=name,
        email=email,
        age=age,
        pwd=secure_password,
        token=token,
        verified=False
    )
    db.session.add(new_user)
    db.session.commit()
    return ''

@app.route('/verified/<string:token>')
def verified(token):
    user = db.session.query(User).filter_by(token=token).first()
    if user:
        print('dupa')
        user.verified = True
        db.session.commit()
    return ''

if __name__ == '__main__':
    # Two lines below required only once, when creating DB.
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
