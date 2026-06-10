import re
import subprocess
import time
from playsound import playsound
import eel
import os
from engine.config import ASSISTANT_NAME 
from engine.command import speak
from engine.helper import remove_words  
from engine.db import cursor
import pywhatkit

# conn = sqlite3.connect("optimus.db")
# cursor = conn.cursor()

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


# def findContact(query):
#     words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
#     query = remove_words(query, words_to_remove)

#     try:
#         query = query.strip().lower()
#         cursor.execute('SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?', ('%' + query + '%', query + '%'))
#         results = cursor.fetchall()
#         print(results[0][0])
#         mobile_number_str = str(results[0][0])

#         if not mobile_number_str.startswith('+91'):
#             mobile_number_str = '+91' + mobile_number_str

#         return mobile_number_str, query
#     except:
#         speak('User not exists in your contacts!')
#         return 0, 0

def findContact(query):
    print("ORIGINAL QUERY:", query)
    words_to_remove = [
        ASSISTANT_NAME,
        "make",
        "a",
        "to",
        "tu",
        "phone",
        "call",
        "send",
        "message",
        "whatsapp",
        "video"
    ]

    query = remove_words(query, words_to_remove)
    print("AFTER CLEANING:", query)

    try:
        query = query.strip().lower()
        cursor.execute(
            '''
            SELECT mobile_no
            FROM contacts
            WHERE LOWER(name) LIKE ?
            OR LOWER(name) LIKE ?
            ''',
            (
                '%' + query + '%',
                query + '%'
            )
        )

        results = cursor.fetchall()
        print("DATABASE RESULT:", results)

        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str
        return mobile_number_str, query
    except Exception as e:
        print("CONTACT ERROR:", e)
        speak("User not exists in your contacts")
        return 0, 0
    
 
def whatsapp(mobile_no, message, flag, name):
    try:
        if flag == "message":
            speak(f"Sending message to {name}")
            pywhatkit.sendwhatmsg_instantly(
                phone_no=mobile_no,
                message=message,
                wait_time=15,
                tab_close=True,
                close_time=3
            )

            speak(f"Message sent to {name}")
        else:
            speak("Currently only message sending is supported")

    except Exception as e:
        print("WhatsApp Error:", e)
        speak("Unable to send the message")


# def sendWhatsappMessage(query):
#     mobile_no, name = findContact(query)
#     if mobile_no == 0:
#         return

#     speak(f"What message should I send to {name}")

#     from engine.command import takeCommand

#     message = takeCommand()

#     if not message:
#         speak("Message cancelled")
#         return

#     whatsapp(
#         mobile_no,
#         message,
#         "message",
#         name
#     )



def sendWhatsappMessage(query):

    print("STEP 1 - Inside sendWhatsappMessage")

    mobile_no, name = findContact(query)

    print("STEP 2")
    print("Mobile:", mobile_no)
    print("Name:", name)

    if mobile_no == 0:
        print("STEP 3 - Contact Not Found")
        return

    speak(f"What message should I send to {name}")

    from engine.command import takeCommand

    message = takeCommand()

    print("STEP 4")
    print("Message:", message)

    if not message:
        print("STEP 5 - Empty Message")
        return

    whatsapp(
        mobile_no,
        message,
        "message",
        name
    )

    print("STEP 6 - Whatsapp Function Called")