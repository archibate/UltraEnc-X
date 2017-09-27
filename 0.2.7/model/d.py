#!/usr/bin/python

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(ciphertext, sheet):
        plaintext = ''
        for position, character in enumerate(ciphertext):
                if character not in ALPHABET:
                        plaintext += character
                else:
                        decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
                        plaintext += ALPHABET[decrypted]
        return plaintext