#!/usr/bin/python

from random import randint

def generate_otp(sheets, length):
        for sheet in range(sheets):
                with open("uex0.1.5_" + str(sheet) + ".uep","w") as f:
                        for i in range(length):
                                f.write(str(randint(0,26))+"\n")

def load_sheet(filename):
        with open(filename, "r") as f:
                contents = f.read().splitlines()
        return contents

def get_plaintext():
        plaintext = input('Please type your message ')
        return plaintext.lower()

def load_file(filename):
        with open(filename, "r") as f:
                contents = f.read()
        return contents

def save_file(filename, data):
        with open(filename, 'w') as f:
                f.write(data)