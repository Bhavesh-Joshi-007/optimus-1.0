from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dir = "UI/assets/audios/optimus_startup.wav"
    playsound(music_dir)

@eel.expose
def playOptimusInitialised():
    music_dir = "UI/assets/audios/optimus_initialized.mp3"
    playsound(music_dir)

@eel.expose
def playOptimusSwitchUp():
    music_dir = "UI/assets/audios/optimus_switchup.wav"
    playsound(music_dir)

