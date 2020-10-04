import json
import requests


class auth():
    def __init__(self, encoded_secrets):
        self.encoded_secrets = encoded_secrets

    def authenticate(self):
        response = json.loads(requests.post("https://accounts.spotify.com/api/token",
                                            headers={
                                                'Authorization': f'Basic {self.encoded_secrets}'},
                                            data={'grant_type': 'client_credentials'}).content)
        return response['access_token']
