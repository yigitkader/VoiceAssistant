import speech_recognition as sr
from datetime import  datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

recognizer = sr.Recognizer() 

def record(ask = False):
    with sr.Microphone() as source_microphone:
        
        if ask:
            print(ask)
            speak(ask)
            
        audio = recognizer.listen(source_microphone)
        
        #İf a problem occured then show empty string
        voice = ' '  
        
        try:
            voice = recognizer.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            
            speak('Sesi anlayamadım, tekrar söyleyiniz')
            #print('\nUnrecognized the voice!!')
        except sr.RequestError:
            speak('Sistemsel bir hata oluştu')
            #print('\nSystem error occured !!')   
        
        return voice



def response(voice):
    # How are you ?
    if 'nasılsın' in voice:
        #print('I am fine thank you, What about you ?')
        speak('iyiyim teşekkür ederim')
    
    # What time is it ?     
    if 'saat kaç' in voice: 
        #print(datetime.now().strftime('%H:%M:%S'))   
        speak(datetime.now().strftime('%H:%M:%S'))
        
    # Search
    if 'arama yap' in voice:
        search_key = record('Ne aramak istiyorsun ? ')     
        url = 'https://google.com/search?q='+search_key
        #print('Tarayıcı açılıyor ..')
        
        speak('Tarayıcı açılıyor')
        webbrowser.get().open(url)
        #print(search_key+ ' için bulduklarım ..')
        speak(search_key+ ' için bulduklarım')

    # Stop        
    if 'kapat' in voice:
        print('Görüşürüz , Çav :))')
        speak('Görüşürüz , Çav ')
        exit()


def speak(sentence):
    tts = gTTS(sentence,lang='tr')
    random_val = random.randint(1,10000)
    file = 'audio-'+str(random_val)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)



# How can i help you ? 
print('Started ...')
speak('Nasıl yardımcı olabilirim')
#time.sleep(1)
while 1:
    voice = record()
    response(voice)
  