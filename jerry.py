from ctypes import alignment
import pyttsx3
from playsound import playsound
from pyautogui import hotkey,press,write,scroll,position,click
from pyjokes import get_joke
import webbrowser
import threading
import pyaudio
import speech_recognition as sr
import time
import os
from tkinter import *
from PIL import ImageTk,Image
from cv2 import VideoCapture
from random import choice
from datetime import datetime
from pywhatkit import playonyt,info
# webbrowser.open_new_tab(google_search)
loop_start=True
list_of_command=('''Hints :
1)  open cmd/Youtube/Whatsapp
2)  how are you/Hello/who are you
3)  tell me a joke
4)  search on wikipedia
5)  what is ai/ai stands for
6)  Volume up/down/ScrollUp/Down
7)  what can you do/Mute/Unmute
8)  how you are programmed/how do you do it
9)  how the tasks are automated/
how you are sending messeges
10) what is used for voice command
11) how you play video/play Music
12) how you created user interface/
how your task are automated
13) who is you Owner
14) what are the three laws of robotics''')

root=Tk()
label_text="Check"
root.geometry(("1920x1080"))
root.title("Jerry")
bg=PhotoImage(file="g2.png")
def start_time():
    text=time.strftime("%H:%M:%S")
    time_label.config(text=text)
    time_label.after(1000,start_time) 
# file="56.gif"
frames=61
# im=[PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)] 
count=0
def animation():
    global count

    if count==(frames-1):
        count=0
    else:
        # l1.config(image=im[count])
        # time.sleep(0.1)
        count+=1
        # l1.after(100,animation)
def greet():
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    # print(current_time)
    time=current_time.split(":")
    hours=int(time[0])
    try:
        if hours<12 and hours>=0:
            welcome="Good morning ."
        elif hours>=12 and hours<18:
            welcome="Good Afternoon ."
        elif hours>=18 and hours<20:
            welcome="Good Evening ."
        elif hours>=20 and hours<24:
            welcome="Good Night ."
    except:
        welcome="Welcome to your laptop"
    pyttsx3.speak(f"{welcome}")

# root.mainloop()
my_label=Label(root,image=bg,width=1920,height=1080)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
# l1=Label(root,image=im[0],width=430,height=340,bg="black")
# l1.place(x=1410,y=640)
label1=Label(root,text=label_text,font=("Helvetica",20),fg="blue")
label1.place(x=920,y=920)
label2=Label(root,text="Hi, Click on Start",font=("vardana",22),fg="red",bg="lightblue")
label2.place(x=840,y=25)
time_label=Label(root,font=("ds-digital",40,"bold"),bg="black",fg="lightblue",bd=10)
time_label.place(x=40,y=130)
l2=Label(root,text="",font=("Times",15),fg="blue",bg="black")
l2.place(x=30,y=400)
l2.config(text=list_of_command,fg="lightblue",font=("times",18,))
start_time()
def gettime():
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    # print(current_time)
    time=current_time.split(":")
    hours=int(time[0])
    try:
        if hours<12 and hours>=0:
            welcome="Good morning ."
        elif hours>=12 and hours<18:
            welcome="Good Afternoon ."
        elif hours>=18 and hours<20:
            welcome="Good Evening ."
        elif hours>=20 and hours<24:
            welcome="Good Night ."
    except:
        welcome="Welcome to your laptop"
    pyttsx3.speak(welcome)
    # print(type(current_time))
    pyttsx3.speak(f"{welcome}, Current time if {current_time}")
    return current_time
    
def givecommand():
    global loop_start
    google_default="https://www.google.com/search?q="
    youtube_default="https://www.youtube.com/results?search_query="
    whatsapp_default="https://web.whatsapp.com/results?search_query="
    press_key=""
    press_key=""
    r=sr.Recognizer()
    greet()
    animation()
    
    while loop_start:
        try:
            with sr.Microphone() as source:
                # print("Listening...")
                label2.config(text="Listening...",fg="blue")
                animation()
                r.adjust_for_ambient_noise(source=source,duration=0.4)
                audio=r.listen(source)
                label2.config(text="Recognizing...",fg="green")
                # print("Recognizing....")
                recognize_command="Recognizing...."
                command=r.recognize_google(audio)
                # print(command)
                command_text=command
                label1.config(text=command)
                if command=="exit" or command=="Bye" or command=="By":
                    pyttsx3.speak("okay sir ,Bye have a nice day")
                    break
                elif command=="hello":
                    pyttsx3.speak("Hello , What i can do for You?")
                elif "press" in command:
                    press_key=command.split()
                    if len(press_key)==2:
                        press(f"{press_key[1]}")
                    elif len(press_key)==3:
                        hotkey(f"{press_key[1]}",f"{press_key[2]}")
                elif command=="open cmd" or command=="open command prompt":
                    os.system("start cmd")
                elif command=="how are you":
                    a=["i am fine sir , Ready for task","i am good now , You can give me command","fine sir","i am fine,what i can do for you?"]
                    choices=choice(a)
                    pyttsx3.speak(choices)
                elif command=="tell me a joke" or command=="can you tell a joke" or ("another joke" in command):
                    a=get_joke()
                    pyttsx3.speak(a)
                elif "search on wikipedia" in command:
                    find=command.split("search on wikipedia")
                    search=find[1]
                    a=info(search,lines=5)
                    pyttsx3.speak(a)
                elif command=="what time is now":
                    gettime()
                elif command=="play song" or command=="play music":
                    # playsound("Music.mp3")
                    os.system("Music.mp3")
                elif command=="change tab": 
                    hotkey("alt","tab")          
                elif command=="volume up":
                    press("volumeup")
                elif command=="volume down":
                    press("volumedown")
                elif command=="mute" or command=="unmute":
                    press("f1") 
                elif command=="scroll down":
                    click(1058,151)
                    scroll(-30)
                elif command=="scroll up":
                    click(1058,151)
                    scroll(30)
                elif command=="open chrome":
                    webbrowser.open("www.google.com")
                elif command=="hello":
                    pyttsx3.speak(" Hello     ")
                elif command=="who are you" or command=="what is your name":
                    pyttsx3.speak("I  am  your  Laptop   assistence , You   can   call Me   Jerry.")
                elif command=="define ai" or command=="ai full form" or command=="ai stands for":
                    pyttsx3.speak("ai means artificial intelligence")
                elif command=="what do mean by ai" or command=="what is ai" or command=="what is artificial intelligence" or command=="what do mean by artificial intelligence":
                    pyttsx3.speak("artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry. ")    
                elif command=="who made you" or command=="who is your owner":
                    pyttsx3.speak("My Owner is  sir, He made me with her Two Friends under the guidance of her professer Mittal Desai")
                elif command=="who am i":
                    pyttsx3.speak("You are one of my Creator sir ")
                elif command=="you are an idiot":
                    pyttsx3.speak("Sorry sir I Apologize")
                elif command=="what are the three laws of robotics" or command=="what are the three laws of robotic":
                    pyttsx3.speak('''First Law
                    A robot may not injure a human being or, through inaction, allow a human being to come to harm.
                    Second Law
                    A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
                    Third Law
                    A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.''')    
                elif command=="what you can do for me" or command=="what can you do" or command=="what are your features jerry":
                    pyttsx3.speak('''1) i can open cmd/Chrome/Youtube/Whatsapp
                                    2)you can ask me how are you/Hello/who are you
                                    3) i can tell you a joke
                                    4) i can search on wikipedia for you
                                    5) i can tell you time
                                    6)  i can  up volume and down or ScrollUp Scroll Down or Mute Unmute
                                    7) i can tell you what is ai or define ai
                                    8) i can tell how i am programmed
                                    9) how i automated my tasks
                                    10) what is used for voice command
                                    11) how i play video on youtube or i can play Music
                                    12) how my GUI is developed
                                    13) who is my owner
                                    14) What are three laws of robotic and many more''')    
                elif command=="how are you doing" or command=="how are you doing today ":
                    pyttsx3.speak("I'm doing Great,How are doing")    
                elif command=="who was Martin Luther King" or command=="tell me about martin luther king": 
                    pyttsx3.speak("martin luther king was an African American Baptist minister and activist who became the most visible spokesperson and leader in the American civil rights movement from 1955 until his assassination in 1968.")
                elif command=="i'm doing great" or command=="i'm good ":
                    pyttsx3.speak("oh thats Great how can i help you sir")  
                elif command=="get lost":
                    pyttsx3.speak("Sorry sir for your Inconvenience I Apologize")    
                elif command=="can i ask you something":
                    pyttsx3.speak("yes sure sir how can i help you") 
                elif command=="open youtube" or command=="youtube":
                    webbrowser.open("www.youtube.com")
                elif command=="open whatsapp" or command=="whatsapp":
                    webbrowser.open("web.whatsapp.com")    
                elif command=="open prime video" or command=="amazon prime video":
                    webbrowser.open("https://www.primevideo.com/storefront/tv/ref=atv_nb_sf_tv")     
                elif command=="Jerry":
                    pyttsx3.speak("Yes  ")
                elif command=="close this":
                    hotkey("alt","f4")      
                elif command=="what is time now":
                    gettime()
                elif command=="what are you doing":
                    a=["I am waiting for your command sir","I am ready for do task ,give me task","I am ready for get your command"]
                    choices=choice(a)
                    pyttsx3.speak(choices)
                elif "play on youtube" in command:
                    find=command.split("play on youtube")
                    search=find[1]
                    youtube_search=youtube_default+search 
                    playonyt(youtube_search)
                elif "search on youtube" in command or command=="open youtube":
                    find=command.split("search on youtube")
                    search=find[1]
                    youtube_search=youtube_default+search
                    webbrowser.open_new_tab(youtube_search)
                elif "search" in command:
                    find=command.split("search")
                    search=find[1]
                    google_search=google_default+search
                    webbrowser.open_new_tab(google_search) 
                elif "open" in command:
                    press("win")
                    find=command.split("open")
                    search=find[1]
                    write(search,interval=0.1)
                    press("enter")
                elif command=="how to play video on youtube":
                    pyttsx3.speka("for play video on youtube you can give me command like this, play on youtube new song")
                elif command=="how you are build" or command=="how you are programmed" or command=="have you programmed" or command=="how do you do it":
                    pyttsx3.speak("I am made using Python language And other pakages like speech recognizer,tkinter,pyautogui,pyttsx3 and pywhatkit.You can see hint on top right corner of screen.")
                    l2.config(text=choice(["Speech Recognizer - Recognize the speech and voice.",
                                      "Tkinter - Tkinter is used for creating GUIs.",  
                                      "pyautogui - Used for automate tasks.",
                                     # "pyttsx3 - Computer voices.",
                                      "pywhatkit - used for opening youtube \nvideos,sending whatsapp massages"]))
                                    #   "pywhatkit - used for opening youtube \nvideos,sending whatsapp massages"]))
                elif command=="how your task are automated":
                    pyttsx3.speak("My task is Automated By using Programming and some Libraries of python. Mainly by using pyautogui.")
                elif command=="how you created user interface" or command=="how your user interface is developed" or command=="have you created user interface" :
                    pyttsx3.speak("Tkinter is used for creating GUI applications using Python.")
                elif command=="how you are sending messeges"or command=="how do you play video ":
                    pyttsx3.speak("pywhatkit is used for opening youtube videos,sending whatsapp masseges etc.")
                elif command=="what is used for voice commands" or command=="what is used for voice command": 
                    pyttsx3.speak("Pyttsx3 named computer voice used for voice commans , Like me.")
                elif command=="how the tasks are automated" or command=="how automatations are done":
                    pyttsx3.speak("Pyautogui is used for automate computer tasks.")
                else:
                    pyttsx3.speak(command)
        except sr.UnknownValueError:
            choice1=("again speak","can't here","Sorry!!","Please speak again","Sorry i dont't understand")
            pyttsx3.speak(choice(choice1))
        except IndexError:
            pyttsx3.speak("Please try again")

# givecommand()
def stop():
    global loop_start
    loop_start=False
def terminate():
    global thereis
    global loop_start
    loop_start=False
    thereis=False
    root.destroy()
    exit()
start_button=Button(root,text="Start",font=("times",20),fg="green",bg="lightgrey",command=threading.Thread(target=givecommand).start)
start_button.place(x=840,y=520)
end_button=Button(root,text="Stop",font=("times",20),fg="red",bg="lightgrey",command=stop and terminate)
end_button.place(x=1020,y=520)
root.protocol("WM_DELETE_WINDOW", stop and terminate)
root.mainloop()