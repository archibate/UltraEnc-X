#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et

'''
 crypt.py  sv0.1  (C)   2017  A BoxLab CTO - Peng YuBin
  
  Type by Hand, All by Original, Including the Algorithm.
  
  Xor-Shift Cryption Core Impelementation.

'''


from model.requirements import filldefault


def encrypt(xs, ks):
    rs = []
    ys = filldefault(xs, default=0)
    
    for i, (x, k) in enumerate(zip(xs, ks)):
        a = ys[i - k]
        rs.append(x ^ a)
    
    return rs


def decrypt(xs, ks):
    rs = []
    
    for x, k in zip(xs, ks):
        try:
            a = rs[-k]  # we assmue that k > 0
        except IndexError:
            a = 0
        rs.append(x ^ a)
    
    return rs
