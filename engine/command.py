import pyttsx3

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

def speak(text):
    engine = pyttsx3.init('nsss')
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[19].id)
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()

speak("Welcome Back Boss!")