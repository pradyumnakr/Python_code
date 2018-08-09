#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:59:53 2018

@author: pradyumna
"""

epsilon=0.01
y=30
guess=y/2.0
numGuesses=0

while abs(guess*guess -y)>=epsilon:
    numGuesses+=1
    guess=guess-(((guess**2)-y)/(2*guess))
print("numGuesses= "+str(numGuesses))
print('square root of ' +str(y) + ' is about '+ str(guess))