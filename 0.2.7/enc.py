#!/usr/bin/python
import time
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)

print ('=========================\nWelcome to use Ultra Enc X');
print ('Version:0.1.5 Beta');
print ('Made by Box Technology\n=========================');
print ('Loading Files...');
time.sleep (3);
print ('Checking...');
time.sleep (1.5);
print ('-------------------------');

from random import randint
from model.main import generate_otp
from model.main import load_sheet
from model.main import get_plaintext
from model.main import load_file
from model.main import save_file
from model.e import encrypt
from model.d import decrypt

def menu():
        choices = ['1', '2', '3', '4']
        choice = '0'
        while True:
                while choice not in choices:
                        print('What would you like to do?\n----------------------------------------')
                        print('[1]. Create new UE X cdoe book(UEcb)   |')
                        print('[2]. Encrypt a message                 |')
                        print('[3]. Decrypt a message                 |')
                        print('[4]. Quit Ultra Enc X(or "exit")       |')
                        print('[5]. For More Help                     |\n----------------------------------------')
                        choice = input('Please enter 1,2,3,4 or 5 and press Enter \n')
                        if choice == '1':
                                sheets = int(input('How many UEcb would you like to create?\n '))
                                length = int(input('What will be your maximum message length?\n '))
                                generate_otp(sheets, length)
                        elif choice == '2':
                                filename = input('Enter the filename of the UEcb you want to use.\n ')
                                sheet = load_sheet(filename)
                                plaintext = get_plaintext()
                                ciphertext = encrypt(plaintext, sheet)
                                filename = input('Enter the name of the decoder.\n ')
                                save_file(filename, ciphertext)
                        elif choice == '3':
                                filename = input('Type in the filename of the UEcb you want to use.\n ')
                                sheet = load_sheet(filename)
                                filename = input('Type in the name of the file to be decrypted\n' )
                                ciphertext = load_file(filename)
                                plaintext = decrypt(ciphertext, sheet)
                                print('The message reads:')
                                print('==============================')
                                print(plaintext)
                                print('==============================')
                        elif choice == '4':
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
                        choice = 'exit'
                        exit()
                        choice = '0'


menu()