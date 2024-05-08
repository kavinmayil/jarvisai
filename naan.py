import pyttsx3
import pywhatkit as kit
import datetime
import speech_recognition as sr
import pyaudio
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again, please")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Shri, please tell me how can I help you")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "open cmd" in query:
            path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)
        elif "play video on youtube" in query:
            speak("Which video shall I play for you?")
            video_query = takecommand()
            kit.playonyt(video_query)
        elif "open google chrome" in query:
            speak("What can I search for you?")
            search_query = takecommand()
            kit.playonyt(search_query)
