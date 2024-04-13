from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")

tts = gTTS(text)
tts.save("output.mp3")