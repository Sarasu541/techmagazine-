import tkinter as tk
import datetime
import speech_recognition as sr
from googletrans import Translator
from tkinter import messagebox
from langdetect import detect 


def is_active_time():
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(21, 30)
    end_time = datetime.time(22, 0)
    return start_time <= current_time <= end_time


def listen_and_translate():
    if not is_active_time():
        messagebox.showinfo("System source","Taking rest, see you tomorrow!")
        return

    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Listening","Please speak in English")
        audio = recognizer.listen(source)

    try:
        
        english_text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {english_text}")

        
        detected_language = detect(english_text)
        print(f"Detected Language: {detected_language}")

        
        if detected_language != 'en':
            messagebox.showinfo("Error", "Sorry, Only english audio is supported. Please speak in English.")
            return

       
        translator = Translator()
        hindi_text = translator.translate(english_text, src='en', dest='hi').text
        print(f"Translated Hindi Text: {hindi_text}")
        output_label.config(text=hindi_text)

    except sr.UnknownValueError:
        messagebox.showinfo("Error", "Sorry, I could not understand. Please repeat.")
    except sr.RequestError:
        messagebox.showinfo("Error", "Could not connect to the service. Try again later.")


root = tk.Tk()
root.title("Voice Translator")

label = tk.Label(root, text="English to Hindi  Translator", font=("Arial", 15))
label.pack(pady=12)

translate_button = tk.Button(root, text="Start Translation", command=listen_and_translate, font=("Arial", 13))
translate_button.pack(pady=30)

output_label = tk.Label(root, text = "", font=("Arial", 13), wraplength=400)
output_label.pack(pady=12)

root.mainloop()
