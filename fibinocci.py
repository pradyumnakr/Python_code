#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:15:21 2018

@author: pradyumna
"""

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(5))