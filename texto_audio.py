from gtts import gTTS
from playsound import playsound

language = 'pt-br'

audio = gTTS(
    text = input('Digite seu texto para converter em áudio: '), 
    lang= language
    
)

audio.save('audio.mp3')
playsound('audio.mp3')
