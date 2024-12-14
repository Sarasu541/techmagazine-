import tkinter as tk
from googletrans import Translator
import threading


root = tk.Tk()
root.title("Dual Language Translator")
translator = Translator()


def translate_text():
    
    input_text = input_text_box.get()

    
    if len(input_text) < 10:
        output_label.config(text="upload again")
        return

    
    translation_thread = threading.Thread(target = process_translation, args=(input_text,))
    translation_thread.start()


def process_translation(text):
    try:
        
        hindi_translation = translator.translate(text, src='en', dest='hi').text
        french_translation = translator.translate(text, src='en', dest='fr').text
        
        
        output_label.config(text=f"Hindi:{hindi_translation}\nFrench: {french_translation}")
    
    except Exception as e:
        output_label.config(text=f"Error during translation: {str(e)}")


input_label = tk.Label(root, text="Enter English text (10+ letters):")
input_label.pack()

input_text_box = tk.Entry(root, width = 70)
input_text_box.pack()


translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

output_label = tk.Label(root, text="Hindi and French words will appear here", width = 70, height = 10)
output_label.pack()


root.mainloop()
