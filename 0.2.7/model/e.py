#!/usr/bin/python

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, sheet):
        ciphertext = ''
        for position, character in enumerate(plaintext):
                if character not in ALPHABET:
                        ciphertext += character
                else:
                        encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
                        ciphertext += ALPHABET[encrypted]
        return ciphertext