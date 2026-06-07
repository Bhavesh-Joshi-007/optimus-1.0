import pyttsx3
import speech_recognition as sr
import eel
from engine import state

# =========================
# SPEECH ENGINE SETUP
# =========================

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty(
    'voice',
    voices[19].id
)
engine.setProperty('rate', 165)
engine.setProperty('volume', 1)


# =========================
# SPEAK FUNCTION
# =========================

@eel.expose
def speak(text):
    engine.say(text)
    engine.runAndWait()

# =========================
# TAKE COMMAND
# =========================

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(
            source,
            duration=1
        )
        audio = r.listen(
            source,
            timeout=10,
            phrase_time_limit=8
        )
    try:
        print("Recognizing...")
        query = r.recognize_google(
            audio,
            language="en-IN"
        )
        print(f"User Said: {query}")
        # speak(query)
        return query.lower()
    except Exception as e:
        print("Error:", e)
        return ""


@eel.expose
def allCommands(query):
    print(query)
    if (
        "search" in query
        or "find" in query
        or "look for" in query
        ):
        from engine.features import searchOnBrowser
        searchOnBrowser(query)
    elif (
        "in chrome" in query 
        or "in google chrome" in query
        or "on google chrome" in query
        or "on chrome" in query
        or "in safari" in query
        or "on safari" in query
        ) and (
        "youtube" in query
        or "google" in query
        or "facebook" in query
        or "instagram" in query
        or "github" in query
        or "chatgpt" in query
        or "whatsapp" in query
        ):
        from engine.features import openWebsite
        openWebsite(query)
    elif "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("Not Run")


@eel.expose
def manualCommand():
    state.WAKEWORD_ACTIVE = False
    query = takeCommand()
    if query:
        allCommands(query)
        
    state.WAKEWORD_ACTIVE = True
    return query