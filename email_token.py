import os
import requests
from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer

load_dotenv()


class EmailToken:

    def __init__(self):
        self.secret = os.environ.get('SECRET_KEY')

    def generate_confirmation_token(self, email):
        serializer = URLSafeTimedSerializer(self.secret)
        return serializer.dumps(email, salt=self.secret)

    def confirm_token(self, token, expiration=3600):
        serializer = URLSafeTimedSerializer(self.secret)
        try:
            email = serializer.loads(
                token,
                salt=self.secret,
                max_age=expiration
            )
        except:
            return False
        return requests.get(f'http://127.0.0.1:5000/verified/{token}')
