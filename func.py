#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:59:55 2018

@author: pradyumna
"""

def fun_a():
    print('inside fun_a')
def fun_b(y):
    print('inside fun_b')
    return y
def fun_c(z):
    print('inside fun_c')
    return z()
print(fun_a())
print(5+fun_b(2))
print(fun_c(fun_a))
    