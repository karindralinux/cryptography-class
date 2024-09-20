import streamlit as st

def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            cipher_text += char
    return cipher_text

def playfair_encrypt(plain_text, key):
    def create_matrix(key):
        key = key.upper().replace("J", "I")
        matrix = []
        for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)

    matrix = create_matrix(key)
    plain_text = plain_text.upper().replace("J", "I")
    cipher_text = ""
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i+1] if i+1 < len(plain_text) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            cipher_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text

def hill_encrypt(plain_text, key):

    import numpy as np

    def text_to_numbers(text):
        return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

    def numbers_to_text(numbers):
        return ''.join([chr(num % 26 + ord('A')) for num in numbers])

    key_matrix = np.array([[ord(key[0].upper()) - ord('A'), ord(key[1].upper()) - ord('A')],
                           [ord(key[2].upper()) - ord('A'), ord(key[3].upper()) - ord('A')]])

    plain_numbers = text_to_numbers(plain_text)


    if len(plain_numbers) % 2 != 0:
        plain_numbers.append(plain_numbers[len(plain_numbers)-1])  # Padding jika panjang teks ganjil
    
    cipher_numbers = []
    for i in range(0, len(plain_numbers), 2):
        pair = np.array(plain_numbers[i:i+2])
        encrypted_pair = np.dot(key_matrix, pair) % 26
        cipher_numbers.extend(encrypted_pair)
    
    return numbers_to_text(cipher_numbers)