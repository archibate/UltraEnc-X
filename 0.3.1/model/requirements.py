#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et

'''
 requirements.py  sv0.1  (C)   2017  A BoxLab CTO - Peng YuBin

   Type by Hand, All by Original, Including the Algorithm.
   
   Useful Classes Requirements.

'''


class filldefault(object):
    '''
    input a list and an default value (default is None).
    when indexing (__getitem__) output,
    if index out of range (index < 0 or index >= length),
    the default value will be returned.
    otherwise, return the original value in the list.
    '''
    
    def __init__(self, indexable, default=None):
        self.list = indexable
        self.default = default

    def __getitem__(self, index):
        if index >= 0 and index < len(self.list):
            return self.list[index]
        else:
            return self.default
        

class repeat(object):
    '''
    repeat an iterable object.
    eg. repeat([1,2,3]) will be resulted in
    [1,2,3,1,2,3,1,2,3...]
    the StopIteration should never be raised.
    '''
    
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.iterable)
            return next(self.iter)


def lmap(func, *iterables):
    return list(map(func, *iterables))

