import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
      hour=int(datetime.datetime.now().hour)
      if hour>=6 and hour<=12:
        speak("good morning sir..")
      elif hour>=12 and hour<=18:
        speak("good afternoon") 
      else:
        speak("good evening")    
      speak(" hello I am jarvis Please tell me how can I help you")

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:  {query}\n")

        except Exception as e:
            speak("Say that again please...")
            return "None"
        return query
    
    # def get_random_advice():
    #     res = requests.get("https://api.adviceslip.com/advice")
    #     return res['slip']['advice']
    
if __name__ =='__main__':
    wishMe()
    while True:
         #if 1:
        query = takeCommand().lower()
         

            #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia") 
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/") 
        elif 'open gmail' in query:
            webbrowser.open("https://accounts.google.com/b/0/AddMailService")         
    

        elif 'who creates you' in query:
            speak("Tejas created me")

        #elif "advice" in query:
            #speak("Here's an advice for you, mam")
            #advice = get_random_advice()
            #speak(advice)
           # speak("for your convinience, I am printing it on the screen")
           # print(advice)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strTime("%H:%M:%S")
            speak("The time is {strTime}")

        elif ' how are you' in query:
            speak("I am fine")

        elif 'logout' in query:
            speak("Thank you")
            exit()