import re
import subprocess
from playsound import playsound
import eel
import os
from engine.config import ASSISTANT_NAME 
from engine.command import speak
import pywhatkit as kit 

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


def openCommand(query):
    query = query.lower()
    query = query.replace(ASSISTANT_NAME.lower(), "")
    query = query.replace("open", "")
    query = query.strip()
    print("App Requested:", query)

    APPS = {
        "chrome": "Google Chrome",
        "google chrome": "Google Chrome",
        "vs code": "Visual Studio Code",
        "visual studio code": "Visual Studio Code",
        "vscode": "Visual Studio Code",
        "terminal": "Terminal",
        "finder": "Finder",
        "safari": "Safari",
        "spotify": "Spotify",
        "notes": "Notes",
        "calculator": "Calculator",
    }

    app_name = APPS.get(query)

    if not app_name:
        speak(f"I could not find {query}")
        return
    try:
        speak(f"Opening {app_name}")
        subprocess.run(
            ["open", "-a", app_name],
            check=True
        )
    except Exception as e:
        print("Open Error:", e)
        speak(f"Unable to open {app_name}, {app_name} doesn't exists in our system sir!")


# def openCommand(query):
#     query = query.replace(ASSISTANT_NAME, "")
#     query = query.replace("open", "")
#     query.lower()

#     if query != "":
#         speak("Opening" + query)
#         # os.system('open' + query)
#         # os.system("open -a " + query)
#         print("query is : ", query)
#         subprocess.run(["open", "-a", query.title()])
#     else:
#         speak("not found")

def openWebsite(query):
    query = query.lower()
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "chatgpt": "https://chatgpt.com",
        "amazon": "https://www.amazon.in",
        "netflix": "https://www.netflix.com",
        "gmail": "https://mail.google.com"
    }

    browser = None

    if "in chrome" in query or "in google chrome" in query:
        browser = "Google Chrome"
    elif "in safari" in query:
        browser = "Safari"

    website = None
    website_name = None

    for key, value in websites.items():
        if key in query:
            website_name = key
            website = value
            break
    if not website:
        speak("I could not identify the website.")
        return
    if not browser:
        speak("Please specify Chrome or Safari.")
        return
    try:
        speak(f"Opening {website_name} in {browser}")
        subprocess.run(
            [
                "open",
                "-a",
                browser,
                website
            ],
            check=True
        )
    except Exception as e:
        print("Website Error:", e)
        speak("Unable to open the website.")

# def openWebsite(query):
#     query = query.lower()
#     websites = {
#         "youtube": "https://www.youtube.com",
#         "google": "https://www.google.com",
#         "google chrome": "https://www.google.com",
#         "facebook": "https://www.facebook.com",
#         "instagram": "https://www.instagram.com",
#         "linkedin": "https://www.linkedin.com",
#         "github": "https://www.github.com",
#         "chatgpt": "https://chatgpt.com",
#         "amazon": "https://www.amazon.in",
#         "netflix": "https://www.netflix.com",
#         "gmail": "https://mail.google.com"
#     }

#     browser = None

#     if "in chrome" in query or "in google chrome" in query:
#         browser = "Google Chrome"
#     elif "in safari" in query:
#         browser = "Safari"

#     website = None

#     for key in websites:
#         if key in query:
#             website = websites[key]
#             break

#     if not website:
#         speak("I could not identify the website.")
#         return

#     if not browser:
#         speak("Please specify Chrome or Safari.")
#         return

#     try:
#         speak(f"Opening {key} in {browser}")
#         subprocess.run([
#             "open",
#             "-a",
#             browser,
#             website
#         ])
#     except Exception as e:
#         print(e)
#         speak("Unable to open the website.")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on Youtube")
    kit.playonyt(search_term)



def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None 