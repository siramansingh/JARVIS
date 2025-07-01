# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def processCommand(c):
#     pass
# def speak(text):
#     engine.say(text)        # Use the variable, not the string "text"
#     engine.runAndWait() 
#     # Required to make the speech engine actually speak


# if __name__ == "__main__":
#     speak("Initilizing  Jarvis....")
#     while True:
#         # Listen for the wake word "Jarivs"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
       
#         print("recognizing")    
#         try:
#             with sr.Microphone() as source:
#                 print("Listening....")
#                 audio = r.listen(source, timeout = 3, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                 speak("Ya")
#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis Active")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)
                    
                    
#                     processCommand(c)
                    
                    
                    
                    
            
        
                   
                
           
                
    
                    
               
                    
         
       
       
       
#         except Exception as e:
#             print("error; {0}".format(e))
            

        


