import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
import threading

def speak(text):
    t = threading.Thread(target=_speak, args=(text,))
    t.start()

def _speak(text):
    engine.say(text)
    engine.runAndWait()


recoginer = sr.Recognizer() # use to reconige the speech while speeking
engine = pyttsx3.init()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif"open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif"open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing jarvis.....")
    while True:
        #listening for the weakup word "jarvis"
        #obtain audio from the microphone

        r = sr.Recognizer()
        print("recogizing")

        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=3 , phrase_time_limit=3)      

                 
            word = r.recognize_google(audio)
            print("lol",word)

            if(word.lower()=="Jarvis"):
                speak("ya")
                #listening for command

                with sr.Microphone() as source:
                    print("jarvis active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))