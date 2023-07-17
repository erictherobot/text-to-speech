import os
from gtts import gTTS

def text_to_speech(text, lang='en'):
    file = gTTS(text=text, lang=lang)
    filename = 'speech.mp3'
    file.save(filename)
    
    # play the audio file
    os.system("afplay " + filename)

text_to_speech("Hello, this is a test.")