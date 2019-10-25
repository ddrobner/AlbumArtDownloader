from spotify import spotify
from config import config

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

spotify = spotify()
config = config()



eventHandler = PatternMatchingEventHandler("currentsong.txt", "", "", False)

def onModified(event):
    f = open(f"{config.getDirectory()}\\config.txt")

    track_id = spotify.search("Stardust lucas and steve")
    spotify.download_art(track_id)

eventHandler.on_modified = onModified

fileObserver = Observer()
fileObserver.schedule(eventHandler, config.getDirectory(), False)
fileObserver.start()

try:
    time.sleep(1)
except KeyboardInterrupt:
    fileObserver.stop()
    fileObserver.join()