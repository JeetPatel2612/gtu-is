#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import random
import string

def generate_monoalphabetic_key():
    """Generate a random Monoalphabetic cipher key."""
    letters = list(string.ascii_uppercase)
    key = {}
    for char in string.ascii_uppercase:
        random_char = random.choice(letters)
        key[char] = random_char
        letters.remove(random_char)  # Remove selected character to ensure unique mapping
    return key

def encrypt_monoalphabetic(message, key):
    """Encrypt a message using a Monoalphabetic cipher."""
    message = message.upper()
    encrypted_message = []
    for char in message:
        if char in key:
            encrypted_message.append(key[char])
        else:
            encrypted_message.append(char)  # if character is not in the key, add it as-is
    return ''.join(encrypted_message)

def decrypt_monoalphabetic(encrypted_message, key):
    """Decrypt a message encrypted with a Monoalphabetic cipher."""
    encrypted_message = encrypted_message.upper()
    decrypted_message = []
    reverse_key = {v: k for k, v in key.items()}  # create reverse key for decryption
    for char in encrypted_message:
        if char in reverse_key:
            decrypted_message.append(reverse_key[char])
        else:
            decrypted_message.append(char)  # if character is not in the key, add it as-is
    return ''.join(decrypted_message)

def analyze_frequency(message):
    """Analyze the frequency of characters in a message."""
    frequency = np.zeros((26,), dtype=int)
    for char in message.upper():
        if char.isalpha():
            frequency[ord(char) - ord('A')] += 1
    return frequency

# Generate a random Monoalphabetic key
key = generate_monoalphabetic_key()
print("Generated Monoalphabetic Key:")
print(key)
    
# Encrypt a message
message = input("Enter the message: ")
encrypted_message = encrypt_monoalphabetic(message, key)
print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
    
# Decrypt the message
decrypted_message = decrypt_monoalphabetic(encrypted_message, key)
print("Decrypted Message:", decrypted_message)

# Analyze the frequency of characters in the original and encrypted messages
original_frequency = analyze_frequency(message)
encrypted_frequency = analyze_frequency(encrypted_message)

