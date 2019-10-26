from config import config
from eventHandler import customEventHandler

import time
from watchdog.observers import Observer

config = config()

path = config.getDirectory()
eventHandler = customEventHandler()

fileObserver = Observer()
fileObserver.schedule(eventHandler, path, False)
fileObserver.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    fileObserver.stop()
    fileObserver.join()