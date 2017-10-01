#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et

'''
Unit Test.
'''

from requirements import repeat
from crypt import encrypt, decrypt

test_key = repeat((1,3,2,3,1,2,2,3,1,2,1))
test_msg = (1,7,3,4,6,2,8,2,3,4,1,5,7,3,8,1,3)
test_key = repeat((1,))
test_msg = (1,2,3,4,5,6,7,8,9,10,11,12,13)
test_res = decrypt(test_key, encrypt(test_key, test_msg))
print(test_msg)
print(test_res)
print("they should be absolutely same, didn't it?")
