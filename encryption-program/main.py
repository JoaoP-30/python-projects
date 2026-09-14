# Encryption Program

# Este programa de criptografia permite que o usuário insira uma mensagem e a 
# criptografe usando uma chave gerada aleatoriamente. O usuário também pode descriptografar 
# a mensagem criptografada usando a mesma chave. O programa utiliza uma lista de caracteres 
# que inclui pontuação, dígitos, letras maiúsculas e minúsculas, além de espaços.

import random
import string 

chars = list(string.punctuation + string.digits + string.ascii_letters + " ")

key = chars.copy()

random.shuffle(key)

# ENCRYPT   

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPT   

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")