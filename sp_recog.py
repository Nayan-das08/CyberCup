import smtplib,ssl
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#google speech api name: david
engine = pyttsx3.init('sapi5') #sapi5 is microsoft speech api
voices = engine.getProperty('voices') #main program
engine.setProperty('voice',voices[0].id) 

#speak function will pronounce the string which is passed to it
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishme function will wish you as per the current time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak("good morning!")
    elif hour>=12 and hour<=18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("I am DAVID sir. Please tell me how can i help you !")

#takecommand function will take microphone input from the user and return string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio)
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    port=465
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.sendmail(to,to,content)

if __name__ == "__main__":
    wishMe()
    while True:
     query=takeCommand().lower()

     if 'wikipedia' in query : 
         speak('searching wikipedia...')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)

     elif "open youtube" in query :
         webbrowser.open("youtube.com")

     elif "open google" in query :
         webbrowser.open("google.com")

     elif "open stack overflow" in query :
         webbrowser.open("stackoverflow.com")

     elif "time" in query: 
         strtime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"SIR,THE TIME IS {strtime}")

     elif "code" in query:
         codepath=r"C:\Users\shivansh uppal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
         os.startfile(codepath)

     elif "mail" in query:
         #need to enable less secure apps till then not working
         try: 
             speak("what should i say ?")
             content=takeCommand()
             to = "shivanshway@gmail.com"
             sendEmail(to,content)
             speak("email is sent")

         except Exception as e: 
             print(e)
             speak("sorry sir, email is not sent ")
    
     elif "github" in query:
         webbrowser.open("github.com")
    
     elif "quit" in query:
            speak("good bye sir")
            break
     
     elif "play music" in query:
            music_dir=r"C:\Users\shivansh uppal\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))