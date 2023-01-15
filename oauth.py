import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Oauth:
    def __init__(self, app_credentials):
        self.scope="user-read-playback-state"
        self.app_credentials = app_credentials

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=app_credentials[0], client_secret=app_credentials[1], redirect_uri="http://127.0.0.1:8000/spotify/callback" ,scope=self.scope))

    def get_spotify_instance(self):
        return self.sp