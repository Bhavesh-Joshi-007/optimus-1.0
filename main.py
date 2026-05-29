import eel
from engine.features import *
from engine.command import *

eel.init("UI")

eel.start('index.html', mode='chrome', host='localhost', block=True)

