from email import message
from gc import get_referents
import queue
from re import search
from unittest import result
from grpc import server
from numpy import greater_equal
import pyttsx3
import speech_recognition as sr
import datetime as time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import random
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
from tkinter import *
import urllib.request
from tkinter.filedialog import askopenfilename
from pywikihow import *
import psutil
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    # function to speak a string
    engine.say(audio)
    engine.runAndWait()

def connect(host="https://google.com"):
    """function to check if defice is connected to the internet or not"""
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False 

def wishMe():
    # Function to use the user
    global greet 
    hour = int(datetime.datetime.now().hour)
    strTime = time.strftime("%I:%M %p")
    if hour >=0 and hour <12:
        print(f"Good Morning Alex!Its{strTime}")
        speak(f"Good Morning Alex!Its{strTime}")
        greet = "Morning"

    if hour >=12 and hour <16:
        print(f"Good Afternoon Alex!Its{strTime}")
        speak(f"Good Afternoon Alex!Its{strTime}")
        greet = "Afternoon"    

    else:
        print(f"Good evening Alex!Its{strTime}")
        speak(f"Good evening Alex!Its{strTime}")
        greet = "Evening"        

    speak("I'm Jarvis Sir, Please tell me how may i help you")

def takecommand():
    # function to take the mic input from user and return a string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        speak("Now Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('a.savu.stefan@gmail.com','M3x6m3x6@@@')
    server.sendmail('yourEmail',to,content)
    server.close()

def WakeUp():
    if connect():
        while True:
            query = takecommand().lower()
            if "wake" in query:
                mainloop()
            else:
                print("Gime me the command to wake up") 
                speak("Gime me the command to wake up")         
                continue
    else:
        while True:
            usercommand = input("Enter your command:".lower())
            if "wake" in usercommand:
                mainloop()
            else:
                print("Gime me the command to wake up") 
                speak("Gime me the command to wake up")  
                continue

def recogniseUser():
    pass

def taskExecution():
    #function to execute all functions and comands
    if connect():
        print("Connection available\nVoice Command activated")
        query = takecommand().lower()

        if 'wikipedia' in query:
            try:
                speak('Searching wikipedia....')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences =3)
                printresult = wikipedia.summary(query,sentences =6)
                speak("According to Wikipedia")
                print(printresult)
                speak(result)
            except Exception as we:
                print(we)
                speak("Sorry Alex,i am unable to search it")

    elif 'temperature' in query:
        try:
            speak(f'Feeling{query}...')
            url = f"https://google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f'Feeled{query}is {temp}')
            speak(f'Feeled{query}is {temp}')
        except Exception as te:
            print(te)
            speak("Sorry Alex ,i am unable to feel")

    elif 'how to' in query:
        try:
            max_results = 1
            how_to = search_wikihow(query,max_results,lang="en")
            assert len(how_to) == 1
            how_to[0].print()
            speak("Sorry Alex,i am unable to search")
        except Exception as he:
            print(he)
            speak("Sorry Alex ,i am unable to search")    

    elif 'google' in query:
        try:
            speak("Searching Google...")
            query = query.replace("google it","")
            webbrowser.open_new_tab(f"https://google.com/search?q={query}")
        except Exception as ge:
            print(ge)
            speak("Sorry Alex ,i am unable to search")   
    elif 'google images' in query:
        try:
            speak("Search google Images...")
            query = query.replace("google images","")
            webbrowser.open_new_tab("https://www.google.com/search?={query}&rlz=1C1CHBD_enIN899IN899&sxrf=ALeKk02ECu1APO1sepw6l4hZehc2zYKQ:1611571424971&source=Inms&tbm=isch&sa=X&ved=2ahUKEwjlzsKy87buAhVIfisKHdkYDgQQ_AUoAXoECAIQAw&biw=1536&bih=754")                 
        except Exception as ge:
            print(ge)
            speak("Sorry Alex,i am unable to search images")

    elif "youtube" in query:
        try:
            speak("Searching youtube...")
            query = query.replace("youtube","")
            webbrowser.open_new_tab(f"https://youtube.com/results?search_query={query}")
        except Exception as ge:
            print(ge)
            speak("Sorry Alex,i am unable to search youtube")

    elif 'open youtube' or 'deschide youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' or 'deschide google' in query:
        webbrowser.open("google.com")  
    elif 'open whatsapp' or 'deschide whatsapp' in query:
        webbrowser.open("web.whatsapp.com")           
    elif 'open google' or 'deschide google' in query:
        webbrowser.open("youtube.com") 
    elif 'close chrome' in query or 'quit chrome' in query:
        os.system("taskill/im chrome.exe /f")
    elif 'play music' in query or 'canta ceva ' in query:
        music_dir = 'C:\\Users\\Alex\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'time' in query or 'timpul' in query:
        strTime = time.strftime("%I:%M %p")
        print("Alex,the time is",strTime)
        speak(f"Alex, the time is {strTime}")

    elif 'date' in query or 'data' in query:
        strDate = datetime.datetime.now().strftime("%x")
        print("Alex, its",strDate)
        speak(f"Alex, its {strDate}")

    elif 'day' in query or 'ziua' in query:
        strDay = datetime.datetime.now().strftime("%A")
        print("Alex, its",strDay)
        speak(f"Alex, its {strDay}")

    elif 'open vs code' in query or "let's code" in query:
        codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open file' in query or 'open a file' in query:
        root = Tk()
        root.title("Open a file")
        filePath = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        os.startfile(filePath)
        root.destroy()

    elif 'tell me a joke' in queue or 'baga o gluma' in query:
        joke = pyjokes.get_joke('en','all')
        print(joke)
        speak(joke) 

    elif 'switch window' in query or 'switch the window' in query:
        speak('Switching window')
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.keyUp('alt')

    elif 'minimize all windows' in query or 'minimize all tasks' in query:
        speak('MinMaxing Windows')
        pyautogui.keyDown('win')
        pyautogui.press('d')
        time.sleep(1)
        pyautogui.keyUp('win')

    elif 'refresh tab' in query or 'refresh screen' in query:
        speak('Refreshing...')
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')
        time.sleep(1)
        pyautogui.press('fn')
        pyautogui.press('f5')

    elif 'email to Alex' in query or 'send a email to Alex' in query:
        try:
            speak("What should i say?")
            content = takecommand()
            to = "viper040688@gmail.com"
            sendEmail(to, content) 
            speak('Email has been sent!')
        except Exception as e:
            speak('Sorry Alex i am unable to send this email')

    elif 'send email' in query or 'spam someone' in query:
        try:
            speak("To whom")
            to = input("Enter email adress whom you want to send:")                   
            speak("What should i say?")
            content = input("Enter here what you want to send:")
            sendEmail(to, content)
            speak("Email has been sent")
        except Exception as e:
            speak("Email has not been sent!")

    elif 'take screenshot' in query or 'freeze screen' in query:
        speak("Alex hold the screen ,i am taking the shot")
        img =pyautogui.screenshot()
        print("Choose a name for the shot")
        speak("Choose a name for the shot")
        name = takecommand().lower()
        img.save(f"C:/Users/Alex/Pictures/{name}.png")
        speak("Job Done for you")
    
    elif "hi" in query or 'hello' in query:
        print("Hi i am Jarvis your personal assistant ,let me know Alex if i can help you ")
        speak("Hi i am Jarvis your personal assistant ,let me know Alex if i can help you ")

    elif "who are you" in query or "what is your name" in query:
        tell = ["I'm Jarvis and i am here to do cool tasks for you",""]
        told = random.choices(tell,weights=None, cum_weights=None,k=1)
        print(told)
        speak(told)

    elif "how are you" in query or 'whats up' in query:
        greeting =[f"I'm all good this{greet} and you?",f"i'm good ! How's your{greet}.",f"i'm doing great this{greet} that i'm taking with you.About yourself!","I'm ok.I hope you and your familly are safe and healty.How can i help you?","I'm well,thanks for asking.I hope you're well too",f"i am great this{greet},Thanks!"]
        greeted =random.choices(greeting, weights=None,cum_weights=None,k=1)
        print(greeted)
        speak(greeted)

    elif 'battery' in query or 'power' in query:
        battery = psutil.sensors_battery()
        batteryLife =time.strftime("%H:%M:%S",time.gmtime(battery.secsleft))
        batteryPercentage = battery.percent
        print(f"Alex, our system have{batteryPercentage}percent life")    
        speak(f"Alex, our system have{batteryPercentage}percent life")
        if battery.power_plugged:
            print("We can work ,device is plugged in")
            speak("We can work ,device is plugged in")
        else:
            if batteryPercentage>=75:
                upto75 = f"we have enough power to continue our work for{batteryLife}."
                print(upto75)
                speak(upto75)
            elif batteryPercentage>=50 and batteryPercentage<=75:
                upto30 = "Battery low please conttect the charger" 
                notification.notify(title='Battery Power Less than 50%',message = upto30,app_icon=None,timeout =10,)
                print(upto30)
                speak(upto30)
            elif batteryPercentage>30:
                lessthan30 ="We are drowing ,please help us with the charger or system will shuting down"
                notification.notify(title='Battery Power Less than 30%',message = lessthan30,app_icon=None,timeout =10,)
                print(lessthan30)
                speak(lessthan30)
    
    elif 'quit' in query or 'bye bye' in query:
        print("Quitting Alex, Appreciate your time")
        speak("Quitting Alex, Appreciate your time")
        exit()

    elif 'sleep' in query or 'standby' in query:
        speak("Alex i am here always")
        WakeUp()

    else:
        if query == 'none':
            print("")
        else:
            try:
                speak("Searching It....")
                webbrowser.open_new_tab(f"https://google.com/search?q={query}")
            except Exception as ce:
                print(ce)
                speak("Sorry ,invalid command")

def mainLoop():
    wishMe()
    while True:
        taskExecution()

mainLoop













