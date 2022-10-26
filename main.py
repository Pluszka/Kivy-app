from flask import Flask
from email_token import EmailToken

app = Flask(__name__)
emailToken = EmailToken()

@app.route('/confirm_email/<string:token>')
def confirm(token):
    emailToken.confirm_token(token)
    return "<h3>Thanks for confirming your e-mail. Your account is created.</h3>"


if __name__ == '__main__':
    app.run(debug=True)
