import pyttsx3
import gmapFinder
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import pyaudio
import pyjokes
import time
import random
from email.mime import audio
from errors import VAFunction404

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@org.com', 'your-password')
    server.sendmail('your-email.org.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")

    speak("How can I help you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        ans = r.recognize_google(audio, language='en-gb')
        print(f"User said : {query}\n")

    except Exception:
        speak("Sorry Sir, didn't catch that.")
        print("Say that again please...")
        raise VAFunction404('Request not in defined function: run()')
    return ans

def run():
    run = True
    while run:
        ans = take_command().lower()
        if 'wikipedia' in ans:
            ans = ans.replace('wikipedia', ' ')
            results = wikipedia.summary(ans, sentences=6)
            speak('According to Wikipedia,' + results)

        elif 'open github' in ans:
            speak('ok. opening github...')
            time.sleep(1)
            webbrowser.open('https://github.com')

        elif 'open discord' in ans:
            speak('opening discord...')
            time.sleep(2)
            os.startfile(r"C:\Users\hinas\AppData\Local\Discord\app-1.0.9008\Discord.exe")

        elif 'open bluestacks' in ans:
            speak('opening bluestacks...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\BlueStacks_bgp64\Bluestacks.exe")

        elif 'open fortnite' in ans:
            speak('opening fortnite...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64"
                        r"-Shipping.exe")

        elif 'open word' in ans:
            speak('opening word...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

        elif 'open teams' in ans:
            speak('opening teams...')
            time.sleep(2)
            os.startfile(r"C:\Users\hinas\AppData\Local\Microsoft\Teams\current\Teams.exe")

        elif 'open powerpoint' in ans:
            speak('opening powerpoint...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

        elif 'open outlook' in ans:
            speak('opening outlook...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE")

        elif 'open google' in ans:
            speak('ok. running google chrome...')
            time.sleep(2)
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif 'open youtube' in ans:
            speak('ok. opening youtube...')
            time.sleep(2)
            webbrowser.open("https://youtube.com")

        elif 'search the website' in ans:
            urll = query.replace("search the website", "")
            webbrowser.open(f"https://{urll}.com")

        elif 'time' in ans:
            t = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {t}")

        elif 'date' in ans:
            date = datetime.date.today()
            speak(f"Today is {date}")

        elif 'joke' in ans:
            speak('Coming up with jokes...')
            time.sleep(1)
            joke = pyjokes.get_joke(language='en', category='neutral')
            speak(joke)

        elif 'song' in ans:
            speak('ok, playing music')
            time.sleep(1)
            music_dir = "C:/Users/hinas/Music"
            songs = os.listdir(music_dir)
            print(songs)
            len_of_songs = len(songs)
            random_song = random.randint(0, len_of_songs)
            os.startfile(os.path.join(music_dir, songs[random_song]))

        elif 'send email to school' in ans:
            speak('Who should I send it to?')
            send_to = take_command()
            if 'name' in send_to:
                try:
                    to = 'email@org.com'
                    speak('What should I say?')
                    content = take_command()
                    sendEmail(to=to, content=content)
                except Exception:
                    speak('Sorry I could not send')
                    raise ConnectionError('Could not find email in SMTP server: office365')
                  
            elif 'name2' in send_to:
                try:
                    to = 'email@org.com'
                    speak('What should I say?')
                    content = take_command()
                    sendEmail(to=to, content=content)
                except Exception:
                    speak('Could not send. Sorry')
                    raise ConnectionError('Could not find email in SMTP server: office365')

        elif 'current location' in ans:
            speak(gmapFinder.getCurrentLocation())

        elif 'directions' in ans:
            speak('Where do you want to go?')
            time.sleep(1)
            destination = take_command()
            dir = gmapFinder.getDirection('current', destination)
            speak('Successfully got directions')
            print(dir)
            time.sleep(5)

        elif 'who are you' or 'who made you' in ans:
            speak('I am relevance, your personal assistant, made by the relevance lord, Weeld333.')

        elif 'shutdown' or 'shut down' in ans:
            speak('Goodbye. shutting down...')
            os.system('shutdown -s')

        elif 'goodbye' in ans:
            speak('goodbye sir')
            exit()

        else:
            speak('I did not understand. Try again.')
            raise VAFunction404('Request not in defined function: run()')

if __name__ == "__main__":
    speak("Hello, I'm Relevance")
    time_greeting()
    run()
