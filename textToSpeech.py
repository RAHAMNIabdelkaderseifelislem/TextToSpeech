#pip install gTTS

from gtts import gTTS 
import os

def textToSpeech(text):
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("text.mp3")
    os.system("start text.mp3")

text = input("enter your text here:")

textToSpeech(text)
