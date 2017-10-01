#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)

print ('=========================\nWelcome to Ultra Enc X');
print ('Version:0.3.1 Beta');
print ('Made by Box Technology\n=========================');
print ('Loading Files...');
time.sleep (1);         # wtf??
print ('Checking...');
time.sleep (1);       # wtff!? CEO?
print ('-------------------------');

from random import randint
from model import *   # let model/__init__.py choice what to import.

def definput(prompt, default):
        result = input(prompt + ' [' + default + '] ')
        if result is None or result == '':
                return default
        else:
                return result

def menu():
        choices = ['1', '2', '3', '4']
        choice = '0'
        while True:
                while choice not in choices:
                        print('What would you like to do?')
                        print('----------------------------------------')
                        print('[1]. Create new UE X cdoe book(UEcb)   |')
                        print('[2]. Encrypt a message                 |')
                        print('[3]. Decrypt a message                 |')
                        print('[4]. Quit Ultra Enc X(or "exit")       |')
                        print('[5]. For More Help                     |')
                        print('----------------------------------------')
                        choice = input('Please enter 1,2,3,4 or 5 and press Enter \n')
                        if choice == '1':
                                sheets = int(definput('How many UEcb would you like to create?', '1'))
                                strength = int(definput('What will be your encryption strength?', '4'))
                                length = int(definput('What will be your wrap length?', '256'))
                                generate_otp(sheets, strength, length)
                        elif choice == '2':
                                filename = definput('Which filename of the UEcb do you want to use?', 'uexor_0.uep')
                                sheet = load_sheet(filename)
                                plaintext = get_plaintext()
                                ciphertext = encrypt(plaintext, sheet)
                                filename = definput('Where do I save the encrypted result?', 'encrypted.txt')
                                save_file(filename, ciphertext)
                        elif choice == '3':
                                filename = definput('Which filename of the UEcb do you want to use?', 'uexor_0.uep')
                                sheet = load_sheet(filename)
                                filename = definput('What is the name of the file to be decrypted?', 'encrypted.txt')
                                ciphertext = load_file(filename)
                                plaintext = decrypt(ciphertext, sheet)
                                print('The message reads:')
                                print('==============================')
                                print(plaintext_to_str(plaintext))
                                print('==============================')
                        elif choice == '4':
                                print('exiting UltraEnc-X...')
                                exit()
                        elif choice == '5':
                                print ('\n==============================')
                                print ('Welcome to use UltraEnc X\nNow,Let us learn how to use this Great Program.')
                                print ('First,type the number 1 and Enter,fill out the content of the inquiry.')
                                print ('You can get a file is seem "uep0.txt",and type num 2 and \n    fill out the content of the inquiry to Encrypt a message.')
                                print ('And,if you want to decrypt a message,you should type num 3 and fill out the content of the inquiry.')
                                print ('Type num 4 will kill and exit UltraEnc X.')
                                print ('Last,type num 5 to show this text.')
                                print ('==============================\n')
                        choice = '0'


menu()
