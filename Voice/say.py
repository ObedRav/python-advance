from gtts import gTTS
import os

tts = gTTS('Hello, how are you?')
tts.save('hello.mp3')
os.system('mpg321 hello.mp3')
