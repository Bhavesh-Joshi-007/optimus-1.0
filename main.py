import eel
import threading
import time

from engine.wakeword import startWakeWordDetection
from engine.features import playOptimusInitialised

eel.init("UI")


def boot_system():
    time.sleep(3)
    playOptimusInitialised()
    startWakeWordDetection()

threading.Thread(
    target=boot_system,
    daemon=True
).start()

eel.start(
    "index.html",
    mode="chrome",
    host="localhost",
    block=True
)