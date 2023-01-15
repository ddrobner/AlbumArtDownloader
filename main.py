import time

from spotify import spotify
from config import config

config = config()
spotify = spotify()

while True:
    spotify.download_art()
    # TODO come up with more clever way to update the art when a new track is played
    time.sleep(5)