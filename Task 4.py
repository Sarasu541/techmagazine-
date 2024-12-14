import speech_recognition as sr
from googletrans import Translator
import pyttsx3


recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()


def detect_language(text):
    detected = translator.detect(text)
    return detected.lang


def speak(text, lang):
    engine.setProperty('voice', lang)  
    engine.say(text)
    engine.runAndWait()


def process_voice_input():
    with sr.Microphone() as source:
        print("Listening  speech")
        audio = recognizer.listen(source)
        
        try:
            
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            
        
            lang = detect_language(text)
            print(f"Detected language: {lang}")
            
            
            if lang == 'es':
                translated = translator.translate(text, src='es', dest='en')
                translated_text = translated.text
                print(f"Translated to English: {translated_text}")
                speak(translated_text, 'english')
            elif lang == 'en':
                translated = translator.translate(text, src='en', dest='es')
                translated_text = translated.text
                print(f"Translated to Spanish: {translated_text}")
                speak(translated_text, 'spanish')
        except Exception as e:
            print("Error recognizing speech:", str(e))


while True:
    process_voice_input()
