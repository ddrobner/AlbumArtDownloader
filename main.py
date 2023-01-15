from oauth import Oauth
from spotify import spotify
from sanitizeInput import sanitizer
from config import config
import requests
import shutil

config = config()
spotify = spotify()
sanitizer = sanitizer()

app_credentials = [config.get_client_id(), config.get_client_secret()]

oauth = Oauth(app_credentials)

result = oauth.get_spotify_instance().currently_playing()

art_url = result['item']['album']['images'][0]['url']
image = requests.get(art_url, stream=True)
with open("album.jpg", "wb") as out:
    shutil.copyfileobj(image.raw, out)