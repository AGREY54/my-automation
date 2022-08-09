from re import T
from watchdog.observers import Observer

import time
from watchdog.events import FileSystemEventHandler
import os

folder_to_track = "C:\\Users\\user\\Downloads\\Video"

det_image = "C:\\Users\\user\\Downloads\\images"

images = [".jepg", ".png", ".jpg"]


class mover(FileSystemEventHandler):
    def on_change(self, event):
        with os.scandir(folder_to_track) as entries:
            for entry in entries:
                src = folder_to_track + "/" + entry
                new_destination = det_image + "/" + entry
                name = entry.name
                dest = folder_to_track
                os.rename(src, new_destination)
                if name.endswith(images):
                    dest = det_image
                else:
                    time.sleep(10)
    on_change()


event_handler = mover()
obsever = Observer()

obsever.schedule(event_handler, folder_to_track ,recursive=True)
obsever.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    obsever.stop()

