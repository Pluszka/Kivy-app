from itsdangerous import URLSafeTimedSerializer


class EmailToken:

    def __init__(self, secret_key):
        self.secret = secret_key

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
        return email
