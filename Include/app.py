import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("Вы сказали " + task)
    except sr.UnknownValueError:
        talk("Я Вас не поняла")
        task = command()

    return task

def makeSomething(task):
    if 'open google' in task:
        talk("Уже открываю")
        url = 'https://www.google.com.ua/'
        webbrowser.open(url)
    elif 'open apple' in task:
        talk("Уже открываю")
        url = 'https://www.apple.com/ru/'
        webbrowser.open(url)

    elif 'stop' in task:
        sys.exit()

while True:
    makeSomething(command())