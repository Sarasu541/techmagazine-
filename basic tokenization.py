import re

def basic_tokenizer(text):
    
    text = re.sub(r'[^\w\s]','', text)
    tokens = text.split()
    return tokens

inputtext = "Hello, Good Morning! This is just a formal meeting."
tokens = basic_tokenizer(inputtext)
print(tokens)
