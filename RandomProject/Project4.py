import string
import random

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars) 
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for leter in plain_text:
    if leter in chars:
        index = chars.index(leter)
        cipher_text += key[index]
    else:
        cipher_text += leter
        


print(f"plain_text: {plain_text}")
print(f"cipher_text: {cipher_text}")


#Decypt

cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for leter in cipher_text:
    if leter in chars:
        index = key.index(leter)
        plain_text += chars[index]
    else:
        plain_text += leter
print(f"cipher_text: {cipher_text}")
print(f"plain_text: {plain_text}")



