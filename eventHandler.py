from spotify import spotify
from config import config

import os
from watchdog.events import PatternMatchingEventHandler

spotify = spotify()
config = config()

path = config.getDirectory()

class customEventHandler(PatternMatchingEventHandler):

    patterns = ["*/currentsong.txt"]


    def on_modified(self, event):
        with open(f"{path}\\currentsong.txt", "r") as f:
            title = f.readline().strip("\n")
        if title:
            track_id = spotify.search(title)
            spotify.download_art(track_id)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Current Song: {title}")