import requests
import shutil
import sys
from spotipy.oauth2 import SpotifyOauthError

from config import config
from oauth import Oauth


class spotify():
    def __init__(self):
        self.config = config()
        self.oauth = Oauth(self.config.get_client_id(), self.config.get_client_secret())
        self.sp = self.oauth.get_spotify_instance()
        self.previous_request = {"item" : ""}

        self.artist_name = ""
        self.track_name = ""


    def download_art(self):
        try:
            self.track = self.sp.currently_playing()
            if (self.track['item'] != self.previous_request['item']):
                self.image_url = self.track['item']['album']['images'][0]['url']
                image = requests.get(self.image_url, stream=True)
                with open('album.jpg', 'wb') as out_file:
                    shutil.copyfileobj(image.raw, out_file)
            self.previous_request = self.track
        except SpotifyOauthError:
            self.Oauth.refresh_access()
            self.sp = self.Oauth.get_spotify_instance()
        except:    
            print("Failed to get album art from Spotify's servers")
        if len(sys.argv) < 2 or sys.argv[1] != "--skip-name":
            self.artist_name = self.track['item']['album']['artists'][0]['name']
            self.track_name = self.track['item']['album']['name']
            with open('track.txt', "w+") as f:
                f.write(f"{self.artist_name} - {self.track_name}")
        