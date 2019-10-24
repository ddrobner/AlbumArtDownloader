import requests
import json
import shutil

from auth import auth

class spotify():
    def __init__(self):
        self.AUTHENTICATION_STRING = "YzRhNWI4NzhlMmI3NGNmODg1YjI4NDNhMTQyODFkYmM6YjE2YzgwZGM1M2MzNDE5NDg3ZGE3MWUxYmU0ZmEyY2E="
        self.authenticator = auth(self.AUTHENTICATION_STRING)
        self.access_token = self.authenticator.authenticate()

    def search(self, title):
        self.result = json.loads(requests.get(f"https://api.spotify.com/v1/search?q={title}&type=track", headers={'Authorization' : f"Bearer {self.access_token}"}).content)
        return  self.result['tracks']['items'][0]['id']

    def download_art(self, album_id):
        self.album = json.loads(requests.get(f"https://api.spotify.com/v1/tracks/{album_id}", headers={'Authorization': f"Bearer {self.access_token}"}).content)
        self.image_url =  self.album['album']['images'][0]['url']
        image = requests.get(self.image_url, stream=True)

        with open('album.jpg', 'wb') as out_file:
            shutil.copyfileobj(image.raw, out_file)
