# ==== Importing all the necessary libraries
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk
import wikipedia
import os
import random
import ctypes
import pyjokes


# ==== Class Assistant
class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="background.vass.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="frame_vass.png")
        left = Label(self.root, image=self.centre).place(x=200, y=200,width=200,height=200)

        # ====start button
        start = Button(self.root, text='START', font = ("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font = ("times new roman", 14), command=self.close_window).place(x=350, y=520)

  

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            assname ="Ryan"   
            speak('Hello there,' + wish+' I am your voice assistant '+assname)
            print('Hello there,' + wish+' I am your voice assistant '+assname)
            # ==== Wish End
        # 
        def user_name():
            speak("What should i call you ")
            uname = take_command()
            print("Welcome,"+uname+"  How can i Help you")
            speak("Welcome ")
            speak(uname)
            speak("How can i Help you")
            
        # ==== Take Command
    
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except:
                pass

        # ==== Run command
        def run_command():
            instruction = take_command()
            print(instruction)
            assname="Ryan"
            try:
                if 'who are you' in instruction or 'hu r u' in instruction:
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction or 'do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction or 'time' in instruction :
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is' + time)

                elif 'open google' in instruction or 'google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('google.com')
            
                elif 'open youtube' in instruction or 'youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction or 'facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                elif 'open st joseph' in instruction :
                    speak('Opening saint josephs college for women website')
                    webbrowser.open('https://stjosephscollegevisakhapatnam.ac.in')

                elif 'open python geeks' in instruction or 'python website' in instruction:
                    speak('Opening PythonGeeks')
                    webbrowser.open('pythongeeks.org')

                elif 'open linkedin' in instruction or 'linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction or 'gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                
                elif 'open cs department' in instruction:
                    speak('opening cs department website' )
                    webbrowser.open('https://computer-science-4073342.evlop.me/')
                    
                elif 'open stack overflow' in instruction or 'stack overflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')

                elif 'wikipedia' in instruction:
                    speak('Searching Wikipedia...')
                    instruction = instruction.replace("wikipedia", "")
                    results = wikipedia.summary(instruction, sentences = 5)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'play music' in instruction or "play song" in instruction:
                    speak("Here you go with music")
                    # music_dir = "G:\\Song"
                    music_dir = r"D:\ai\voice_assistantgfg\songs"
                    songs = os.listdir(music_dir)   
                    random = os.startfile(os.path.join(music_dir, songs[7]))
                
                elif 'joke' in instruction or 'jokes' in instruction:
                   joke=pyjokes.get_joke()
                   print(joke)
                   speak(joke) 

                elif 'news' in instruction:
                    speak('Here are some headlines from the Times of India,Happy reading')  
                    webbrowser.open('https://timesofindia.indiatimes.com/home/headlines')

            
                elif 'lock window' in instruction:
                     speak("locking the device")
                     ctypes.windll.user32.LockWorkStation()   

                elif 'shutdown' in instruction:
                    speak("Thanks for giving me your time")
                    speak('I am shutting down')
                    self.close_window()
                    exit()
                    return False
                    

                
               
                else:
                    speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True

        # ====Default Start calling
        start()
        user_name()
        # ====To run assistance continuously
        while True:
            if run_command():
                run_command()
            else:
                break


    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== create tkinter window
root = Tk()


# === creating object for class
obj=assistance_gui(root)

# ==== start the gui
root.mainloop()