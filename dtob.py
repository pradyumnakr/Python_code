#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:34:45 2018

@author: pradyumna
"""

num=3

if num<0:
    isNeg=True
    numm=abs(num)
else:
    isNeg=False
result=''
if num==0:
    result='0'
while num>0:
    result=str(num%2)+result
    num//=2
print(result)
if isNeg:
    result='-'+result