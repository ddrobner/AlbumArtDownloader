import json
import requests

class auth():
    def __init__(self, encoded_secrets):
       self.encoded_secrets = encoded_secrets

    def authenticate(self):
        return requests.post("https://accounts.spotify.com/api/token",
                             headers={'Authorization:' : f'Basic {encoded_secrets}'},
                             data={'grant_type': 'client_credentials'})

