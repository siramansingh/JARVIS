import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import time
import os

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "12f52d35dfeb4c8aa6e6d35e30937eb1"


def speak_old(text):
    engine.say(text) # Use the variable, not the string "text"
    engine.runAndWait() 
    
    
    
    
 # using gtts   
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    

    # Initialize the mixer module
    pygame.mixer.init()

    # Load your MP3 file (replace with your own file path)
    pygame.mixer.music.load("temp.mp3")

    # Start playing the music
    pygame.mixer.music.play()

    # Optional: Wait for the music to finish (or run indefinitely)
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    pygame.mixer.music.unload()    
    os.remove("temp.mp3")
        

    
   
    
#openai
def aiProcess(command):
    client = OpenAI(api_key="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",
    )

    chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system", "content": "You are virtual assistant named jarvis skilled in general task like alexa and Google Cloud. Give short response plesase",
            "role":"user", "content": command
        }
    ]
    
    )

    return chat_completion.choices[0].message.content    


def processComand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")    
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")  
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")  
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
        
    elif"news" in c.lower():
       
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = response.json()
        # Extract and speak all titles
        if data["status"] == "ok":
            articles = data["articles"]
            print("Top Headlines:\n")
            engine.say("Here are the top headlines for today.")
            for i, article in enumerate(articles, start=1):
                title = article["title"]
                print(f"{i}. {title}")
                engine.say(f"Headline {i}. {title}")
            engine.runAndWait()
        else:
            print("Failed to fetch news.")
            engine.say("Failed to fetch news.")
            engine.runAndWait()
        
    else:
        # Lets OpenAI Handle the request  
        output = aiProcess 
        speak(output)
       
        



       
                
          # pass

if __name__ == "__main__":
    speak("Initilizing  Jarvis....")
    while True:
        # Listen for the wake word "Jarivs"
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing")    
        

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout = 3, phrase_time_limit=1)
        
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Active Jarvis")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    
                    processComand(command)
               
                    
         
       
       
       
        except Exception as e:
            print("error; {0}".format(e))
            

        