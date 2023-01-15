import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Oauth:
    def __init__(self, client_id, client_secret):
        self.scope="user-read-playback-state"
        self.client_id = client_id
        self.client_secret = client_secret
        
        self.auth_manager = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri="http://127.0.0.1:8000/spotify/callback", scope=self.scope)

        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)

    def get_spotify_instance(self):
        return self.sp

    def refresh_access(self):
        self.token_info = self.auth_manager.cache_handler.get_cached_token()
        if self.auth_manager.is_token_expired(self.token_info):
            self.auth_manager = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri="http://127.0.0.1:8000/spotify/callback", scope=self.scope)
            self.sp = spotipy.Spotify(auth_manager=self.auth_manager)