#!/usr/bin/env python
# coding: utf-8

# In[1]:


def caesar_cipher_encrypt(msg, shift):
    ciphertext = ""
    for char in msg:
        if char.isalpha():
            if char.isupper(): #Checks if the character is alphabetic
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    msg = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            msg += shifted_char
        else:
            msg += char
    return msg

msg = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher_encrypt(msg, shift)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)

