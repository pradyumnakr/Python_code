#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:12:10 2018

@author: pradyumna
"""

x=25
epsilon=0.01
numGuesses=0
low=1.0
high=x
ans=(low+high)/2.0
while abs(ans**2-x)>=epsilon:
    print("low is " +str(low)+ 'high is '+str(high)+'ans is '+str(ans))
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
print('numGuesses= '+str(numGuesses))
print(str(ans)+ 'is close to the square root of '+str(x))