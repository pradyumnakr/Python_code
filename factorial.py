#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:47:15 2018

@author: pradyumna
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))