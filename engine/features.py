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


from urllib.parse import quote_plus
import subprocess


def searchOnBrowser(query):
    query = query.lower()
    # =========================
    # DETECT BROWSER
    # =========================
    browser = None

    if (
        "google chrome" in query
        or "chrome" in query
    ):
        browser = "Google Chrome"
    elif "safari" in query:
        browser = "Safari"

    if not browser:
        speak("Please specify Chrome or Safari")
        return

    # =========================
    # CLEAN QUERY
    # =========================

    remove_words = [
        "search",
        "find",
        "look for",
        "on google chrome",
        "in google chrome",
        "on chrome",
        "in chrome",
        "on safari",
        "in safari",
        "using chrome",
        "using safari"
    ]

    search_term = query

    for word in remove_words:
        search_term = search_term.replace(
            word,
            ""
        )

    search_term = search_term.strip()

    if not search_term:
        speak(
            "Please tell me what to search."
        )
        return

    # =========================
    # BUILD SEARCH URL
    # =========================

    search_url = (
        "https://www.google.com/search?q="
        + quote_plus(search_term)
    )

    print("Browser :", browser)
    print("Search  :", search_term)
    print("URL     :", search_url)

    # =========================
    # OPEN IN BROWSER
    # =========================

    try:
        speak(
            f"Searching {search_term}"
        )

        subprocess.run(
            [
                "open",
                "-a",
                browser,
                search_url
            ]
        )
    except Exception as e:
        print(e)
        speak(
            "Unable to perform search."
        )


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
        "gmail": "https://mail.google.com",
        "whatsapp": "https://web.whatsapp.com/"
    }

    # =========================
    # DETECT BROWSER
    # =========================

    browser = None

    if (
        "google chrome" in query
        or "chrome" in query
    ):
        browser = "Google Chrome"
    elif "safari" in query:
        browser = "Safari"

    # =========================
    # CLEAN QUERY
    # =========================
    clean_query = query
    remove_words = [
        "open",
        "on google chrome",
        "in google chrome",
        "on chrome",
        "in chrome",
        "on safari",
        "in safari"
    ]

    for word in remove_words:
        clean_query = clean_query.replace(word, "")

    clean_query = clean_query.strip()

    print("Original Query :", query)
    print("Clean Query    :", clean_query)

    # =========================
    # FIND WEBSITE
    # =========================

    website = websites.get(clean_query)

    if not website:
        speak(f"I could not identify {clean_query}")
        return

    # =========================
    # OPEN WEBSITE
    # =========================

    try:
        speak(f"Opening {clean_query} in {browser}")
        if browser == "Google Chrome":
            subprocess.run([
                "open",
                "-a",
                "Google Chrome",
                website
            ])
        elif browser == "Safari":
            subprocess.run([
                "open",
                "-a",
                "Safari",
                website
            ])
    except Exception as e:
        print("Website Error:", e)
        speak("Unable to open the website.")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on Youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None 