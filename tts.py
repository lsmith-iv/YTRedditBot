import pyttsx3
import os

def text_to_speech(fileName, text):
    filePath = f"{os.getcwd()}/{fileName}.mp3"
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath
