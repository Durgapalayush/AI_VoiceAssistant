import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def calculate(expression):
    try:
        result = eval(expression)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The result is {result}")
        print(f"{current_time} - Result: {result}")
        return f"The result is {result}"
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")
        print("Error:", e)
        return "Sorry, I couldn't calculate that."

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi, I am Alex. How may I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'hello alex' in query:
            speak("Hello sir, how are you?")
        elif 'i am fine' in query:
            speak("That's great, sir")
        elif 'thanks alex' in query:
            speak("You are welcome, sir")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\ayush\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif 'change music' in query:
            music_dir = "C:\\Users\\ayush\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        elif 'open code' in query:
            code_path = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'exit' in query:
            speak("Goodbye!")
            speak("Have a great day, Ayush!")
            break
        elif "pause" in query:
            pyautogui.press("k")
            speak("Video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("Video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("Video muted")
        elif "volume increase" in query:
            pyautogui.press("volumeup")
            speak("Turning volume up, sir")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            speak("Turning volume down, sir")
        elif "finally sleep" in query:
            speak("Going to sleep, sir")
            exit()
        elif "calculate" in query:
            expression = query.replace("calculate", "").strip()
            calculate(expression)
        
