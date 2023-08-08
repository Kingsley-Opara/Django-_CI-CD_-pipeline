from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

# Create your tests here.
class TestDjangoSecretKey(TestCase):
    def test_secret_key_secret(self):
        SECRET_KEY = settings.SECRET_KEY
        try:
            validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'{SECRET_KEY} is not a strong secret key...please ensure you use a stronger key'
            self.fail(f'{msg} {e.messages}')