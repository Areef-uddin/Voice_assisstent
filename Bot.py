#imported all usefull modueles and packages
import os
import webbrowser
import subprocess
from AppOpener import open,close
import openai
import pyttsx3
import speech_recognition as sr
from config import apikey#took openai api key
#here initialized the voice to speak
def Speak(audio):
        en = pyttsx3.init('sapi5')
        voices = en.getProperty('voices')
        en.setProperty('voice', voices[0].id)
        en.say(audio)
        en.runAndWait()

#open function which will take queries and give answer
def chat(query):
    global chatt


    chatt =f'python response for user:{query}\n******\n\n'

    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    texts= response['choices'][0]['text']

    Speak(texts)

    if not os.path.exists('C:\AI\Openai'):
        os.makedirs('C:\AI\Openai')


#for taking response from micrphone
def takeResponse():
        global query

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threshold = 0.7
            audio = r.listen(source)

            query = r.recognize_google(audio,language="en-in")
            print("person", query)
            return query

def restart():
    while True:
        Speak("what can i do for u")

        take = takeResponse()

        given = take.lower()
        sites=[["youtube","https://youtube.com"],["brave","https://brave.com"],["google","http://www.google.com"],["microsoft","http://www.microsoft.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                Speak(f"opening {site[0]}")
                webbrowser.open(site[1])
            elif given == "break":
                break


        #opening application
        applications= [["whatsapp", "whatsapp"], ["video player", "VLC"],
                 ["illustrator", "illustrator"], ["photoshop" ,"photoshop"],["word" ,"winword"],["excel","excel"],["powerpoint","powerpnt"],["notepad","notepad"],["Studio","Visual Studio Code"]]
        for application in applications:
            if f"Open {application[0]}".lower() in query.lower():
                Speak(f"opening {application[0]}")
                open(application[1])
            elif given == "break":
                break



         #closing application
        capplications = [["youtube","youtube"],["whatsapp", "whatsapp"], ["video player", "VLC"],
                        ["illustrator", "illustrator"], ["photoshop", "photoshop"], ["word", "winword"],
                        ["excel", "excel"], ["powerpoint", "powerpnt"], ["notepad", "notepad"],["Studio","Visual Studio Code"]]
        for capplication in capplications:
            if f"close {capplication[0]}".lower() in query.lower():
                Speak(f"close {capplication[0]}")
                close(capplication[1])
            elif given == "break":
                break

        if "hey python" in query.lower():
                Speak("yeah ok")

                chat(query)
        elif given=="shutdown":
            Speak("ok areef system is going to sleep")
            os.system("shutdown /s /t 1")
        elif given=="restart":
            Speak("ok areef system is going to restart or reboot")
            os.system("shutdown /r /t 1")
        elif given=="open a file":
            subprocess.call("A.py", shell=True)
            Speak(f"opened file {given}")
        elif given == "run a file":
            Speak("runninig a file")
            subprocess.run(['notepad.exe', 'DirFile'])
            Speak("file run successfully")

        elif given=="break"or given=="stop":
            Speak("going to mute")
            break
Speak("hi areef ")
restart()
