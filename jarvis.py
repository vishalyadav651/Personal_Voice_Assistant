from wikipedia.wikipedia import random
import pyttsx3
import datetime
import time
from googletrans import Translator
import subprocess
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha
import pyjokes 
import shutil
import cv2
import ctypes
import sys
import json
import requests
from urllib.request import urlopen
from requests import get
import pywhatkit as kit
#from twilio.rest import Client
#from clint.textui import progress




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#It takes microphone input from the user and returns string output (voice into text)
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("unable to recognize your voice")  
        return "None"
    return query


#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    
    else:
        speak("good evening")

    assname =("Jarvis 2 point o. how may i help you")
    speak("I am your Assistant")
    speak(assname)

#asking username
def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")





if __name__=="__main__":
    
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    #usrname()
    
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        #search on wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        #open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

        #open facebook
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        

        #open instagram
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        

        #search on google
        elif 'open google' in query:
            speak("sir what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        
        #open stackoverflow
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")  
        
        #send whatsapp message
        elif 'send whatsapp message' in query:
            kit.sendwhatmsg("+918112524315","this message is sent by jarvis",9,15)
            
        

        #play video on youtube
        elif 'play video on youtube' in query:
            speak("sir what should i play on youtube")
            cy = takeCommand().lower()
            kit.playonyt(f"{cy}")

        #play music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\User\\Desktop\\Documents\\media\\WhatsApp Audio\\Sent'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)   
            os.startfile(os.path.join(music_dir, rd))

        
        #ip address
        elif 'ip address' in query: 
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        
        #whats the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        

        #open vs code
        elif 'open code' in query:
            codePath = "C:\\Users\\Robinhood\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        

        #open notepad
        elif 'open notepad' in query:
            npath ='C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(npath)

        

        #to close any(eg. notepad) application
        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")


        #open command prompt
        elif 'open command prompt' in query:
            os.startfile("cmd")
        

        #open camera
        elif 'open camera' in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                if cv2.waitKey(10) == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()



        #send email to vishal
        elif 'send email to vishal' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "vr000651@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")


        #send a mail
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                speak("whome should i send")
                to = takeCommand().lower()    
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")


        #how are you
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        

        #fine or good's answer
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        

        #change name to
        elif "change my name to" in query:
            query = query.replace("change my name to", "jarvis")
            assname = query
        

        #change name
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
         

        #what is your name
        elif "what is your name" in query or "What is your name" in query:
            speak("       My friends call me jarvis")
            #speak(assname)
            #print("My friends call me", assname)
        

        #exit
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        

        #who made/created you
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Vishal")


        #joke    
        elif 'joke' in query or 'another joke' in query:
            speak(pyjokes.get_joke())


        #temperature
        elif 'temperature' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("internet connection error")

        
        #calculator
        elif "calculate" in query: 
            try:
                speak("what should i calculate?")
                gh = takeCommand().lower()
                res = app.query(gh)
                speak(next(res.results).text)
            except:
                print("internet connection error or invalid data")


        #to exit
        elif 'no thanks' in query:
            speak("thanks for using me sir. have a good day ")
            sys.exit()

        
        #to set alarm
        #elif 'set alarm' in query:
            nn = datetime.datetime.now().strftime("%H:%M:%S")
            if nn==18:
                music_dir = 'C:\\Users\\Robinhood\\Desktop\\media\\WhatsApp Audio\\Sent'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[3]))
            speak("alarm have been set")
        


        #To change wallpaper
        elif 'change background' in query or 'change wallpaper' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "C:\\Users\\Robinhood\\Downloads\\wallpaper2.jpg",
                                                       0)

        #To write a note
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis1.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        


        #To show notes
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis1.txt", "r") 
            print(file.read())
            speak(file.read(6))


        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "bb9654a5badffb867b0a1b47f2bff048"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")

        elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("8Y53A2-VHR466AXR2")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        


        #To locate a location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")


        #To restart the computer
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        
        
        #To restart the computer
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        


        #To log off the computer
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

       

       #for latest news from 
        elif 'news' in query:
             
            try: 
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=in&apiKey=70831eb2902244c0afaba2c050a4cf50")
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news are')
                print("=============== WORLD ============"+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
        
       #to open a file
        elif 'open file' in query:
            speak("sir which file should i search  ")
            listing = os.walk('C://')
            cm = takeCommand().lower()
            cm1 = cm.replace(" ","")
            search_input= cm1.replace("dot",".")
            print (search_input)

            file_found= False
            for root_path, directories, files in listing:
                if search_input in files:
                    file_found= True
                    filepath = os.path.join(root_path,search_input)
                    print("file found at location=")
                    print(filepath)
                    os.startfile(filepath)
            if(not file_found):
                print("file does not exist")


        speak("sir do you have any other work for me?")     
            
        
   