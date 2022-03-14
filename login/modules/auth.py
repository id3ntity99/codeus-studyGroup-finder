from google.oauth2 import id_token
from google.auth.transport import requests
from dotenv import load_dotenv
import os


class IDTokenVerification(object):
    def __init__(self):
        dotenv_path = os.path.abspath("../../.env")
        load_dotenv(dotenv_path)
        self.CLIENT_ID = os.getenv("CLIENT_ID")

    def verify_token(self, token):
        try:
            user_info = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                self.CLIENT_ID,
            )
            return user_info
        except ValueError as e:
            return e


class DummyTokenVerification(object):
    def __init__(self):
        dotenv_path = os.path.abspath("../../.env")
        load_dotenv(dotenv_path)
        self.DUMMY_ID = os.getenv("DUMMY_ID")

    def verify_token(self, token):
        try:
            user_info = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                self.DUMMY_ID,
            )
            return user_info
        except ValueError as e:
            return e


class VerificationFactory(object):
    @staticmethod
    def get_verification_method(is_dummy: bool = False):
        if is_dummy:
            return DummyTokenVerification()
        else:
            return IDTokenVerification()
