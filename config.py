import base64
import os


class config():
    def __init__(self):
        self.client_id = os.environ.get("SPOTIFY_CLIENT_ID")
        self.client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
        self.token = base64.b64encode(str.encode(
            f"{self.client_id}:{self.client_secret}", 'utf-8')).decode('utf-8')

    def getToken(self):
        return self.token

    def get_client_id(self):
        return self.client_id

    def get_client_secret(self):
        return self.client_secret
