import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == '__main__':
    speak("Welcome to RoboSpeaker")
    while(True):
        speak("what do you want me to speak? ")
        x = input("Enter here ")
        if x == "q":
            speak("okay bye bye")
            break
        speak(x)