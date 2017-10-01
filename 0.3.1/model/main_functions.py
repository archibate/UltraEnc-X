#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
impelement the main functions required by enc.py.
'''


from random import randint
from model.requirements import lmap, repeat


def generate_otp(sheets, strength, length):
        for sheet in range(sheets):
                filename = "uexor_%s.uep" % (str(sheet),)
                with open(filename, 'w') as output:
                        for i in range(length):
                                print(randint(1, strength), file=output)


def load_sheet(filename):
        with open(filename, 'r') as sheet:
                contents = sheet.read().splitlines()
        return lmap(int, contents)


def plaintext_to_str(plaintext):
        return ''.join(lmap(chr, plaintext))


def get_plaintext():
        plaintext = input('Please type your message: ')
        return lmap(ord, plaintext)


def load_file(filename):
        with open(filename, 'r') as file:
                contents = file.read().splitlines()
        return lmap(int, contents)


def save_file(filename, data):
        with open(filename, 'w') as file:
                file.write('\n'.join(lmap(str, data)))

