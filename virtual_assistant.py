import speech_recognition as sr
import pyttsx3

listeener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say('I am your Alexa')
engine.say('What Can I do For you')
engine.runAndWait()


try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listeener.listen(source)
        command = listeener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:

           print(command)
except:
    pass