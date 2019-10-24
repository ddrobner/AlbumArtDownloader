import requests

from auth import auth

class spotify():
    def __init__(self):
        self.AUTHENTICATION_STRING = "YzRhNWI4NzhlMmI3NGNmODg1YjI4NDNhMTQyODFkYmM6YjE2Y      zgwZGM1M2MzNDE5NDg3ZGE3MWUxYmU0ZmEyY2E="
        self.authenticator = auth(AUTHENTICATION_STRING)
        self.access_token = authenticator.authenticate()

    def search(self, title):
        self.result = requests.get(f"https://api.spotify.com/v1/search?q={title}&type=track", headers={'Authorization' : self.access_token})
        print(self.result)

    def download_art(self, id):
        track = requests.get(f"https://api.spotify.com/v1/tracks/{id}", headers={'Authorization': self.access_token})
