import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyttsx3
import smtplib
import random
import os

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

engine=pyttsx3.init()                    # initializes pyttsx3

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def speak(text):
    engine.say(text)                     #say() -- spells your words
    engine.runAndWait()                  #runAndWait() -- this holds the engine so that spoken sentances could be listen

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def greetMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")
    speak("I am your personal assistant ! Please tell me how may I help you")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikashs2000@gmail.com', '@Vikash123')
    server.sendmail('vikashs2000@gmail.com', to, content)
    server.close()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening.... ")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising.... ")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said :- {query} \n")
    except:
        print(" Say that again Please ")
        return "None"
    return query

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__=='__main__':
    greetMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open google' in query:
            speak("Opening Google sir")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak("Opening Google Sir")
            webbrowser.open("facebook.com")
        elif 'open youtube' in query:
            speak("Opening Youtube Sir")
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            speak("Playing sir ")
            mus_dir='D:\\music'
            songs=os.listdir(mus_dir)
            x=random.randint(0,len(songs))
            os.startfile(os.path.join(mus_dir,songs[x]))
        elif 'the time' in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {Time}")
        elif 'send email to' in query:
            try:
                speak("What message you want me to send ")
                content=takeCommand()
                to="vikashs2000@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except:
                speak("Sorry can't send this Email")
        elif 'are you' in query:
            speak("I am a virtual assistant made by you")
        elif 'do' in query:
            speak("I can please you by doing your work sir ")
