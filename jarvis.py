import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import smtplib
import os

print("Initializing Friday....")
MASTER = "kuhshahl"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    # speak function will pronounce the string passed to it
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good evening" + MASTER)

    # speak("I am Friday. How may I help you?")


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Can you say that again please")
        query = None
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail("harry@codewithharry.com", to, content)
    server.close()


#  Main program

def main():
    speak("Initializing Friday...")
    wishMe()
    takeCommand()
    query = takeCommand()

    # Logics for executing tasks as per the query
    if 'wikipedia' in query.lower:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url = "https:www.youtube.com"

        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url = "https://www.google.com"

        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower(): 
        # here in reddit i can put any web site that i want just have to write wevside name in place of reddit
        # webbrowser.open("youtube.com")
        url = "https://www.reddit.com"

        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif 'play music' in query.lower():
        songs_dir = "# add music path"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'play music' in query.lower():
        codePath = "# write vs code path"  # c:\\users\\vscode(you have to use double slash for skepping the slash)
        os.startfile(codePath)

    elif 'email to harry' in query.lower():
        try:
            speak("What should i send")
            content = takeCommand()
            to = "kusal@gmail.com"
            sendEmail(to, content)

        except Exception as e:
            print(e)


main()


# speak("hello world")
# This function will wish you as per the current time
def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)

    if hour >=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good evening" + MASTER)

    # speak("I am Friday. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        print("Can you say that again please")
    #     query = None
    # return query

#  Main program

speak("Initializing Friday...")
wishMe()
takeCommand()
