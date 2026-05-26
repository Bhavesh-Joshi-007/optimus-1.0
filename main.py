import os

import eel

eel.init("UI")

# os.system('open -a "Google Chrome" "http://localhost:8000/index.html"')

eel.start('index.html', mode='chrome', host='localhost', block=True)

 