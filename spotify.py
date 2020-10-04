import requests
import json
import shutil

from auth import auth
from config import config


class spotify():
    def __init__(self):
        self.config = config()

        self.AUTHENTICATION_STRING = self.config.getToken()
        self.authenticator = auth(self.AUTHENTICATION_STRING)
        self.access_token = self.authenticator.authenticate()

    def search(self, title):
        try:
            self.result = json.loads(requests.get(f"https://api.spotify.com/v1/search?q={title}&type=track", headers={
                                     'Authorization': f"Bearer {self.access_token}"}).content)
        except:
            # Tokens expire after an hour so it reauthenticates if the request fails (done to avoid a mess keeping track of tokens)
            print("Invalid token... Attemping authentication again")
            self.access_token = self.authenticator.authenticate()
        return self.result['tracks']['items'][0]['id']

    def download_art(self, album_id):
        try:
            self.album = json.loads(requests.get(f"https://api.spotify.com/v1/tracks/{album_id}", headers={
                                    'Authorization': f"Bearer {self.access_token}"}).content)
            self.image_url = self.album['album']['images'][0]['url']
            image = requests.get(self.image_url, stream=True)
        except:
            # Tokens expire after an hour so it reauthenticates if the request fails (done to avoid a mess keeping track of tokens)
            print("Invalid token... Attemping authentication again")
            self.access_token = self.authenticator.authenticate()

        with open('album.jpg', 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)
