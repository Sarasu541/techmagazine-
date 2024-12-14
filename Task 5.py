
import tkinter as tk
from transformers import MarianMTModel,MarianTokenizer
import datetime


model_name = "Helsinki-NLP/opus-mt-en-hi"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


def translate_to_hindi(english_word):
    
    translated = model.generate(**tokenizer(english_word,return_tensors="pt"))
    hindi_word = tokenizer.decode(translated[0],skip_special_tokens=True)
    return hindi_word


def starts_with_vowel(word):
    return word[0].upper() in "AEIOU"


def process_translation():
    word = entry.get()  
    current_time = datetime.datetime.now().hour
    
    
    if starts_with_vowel(word):
        if current_time >= 21 and current_time < 22:
            
            hindi_translation = translate_to_hindi(word)
            result_label.config(text=f"Translated to Hindi:{hindi_translation}")
        else:
            result_label.config(text="Please provide another word")
    else:
        
        hindi_translation = translate_to_hindi(word)
        result_label.config(text=f"Translated to Hindi:{hindi_translation}")

root = tk.Tk()
root.title("English to Hindi Translator")


input_label = tk.Label(root, text="Enter English Word")
input_label.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=10)

translate_button = tk.Button(root, text="Translate",command=process_translation)
translate_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="Translated Hindi Word will appear here")
result_label.pack(padx=10, pady=20)


root.mainloop()



