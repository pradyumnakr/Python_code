#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:34:26 2018

@author: pradyumna
"""

num=int(input("enter the decimal number\n"))
if num<0:
    is_neg=True
    num=abs(num)
else:
    is_neg=False
result=" "
if num==0:
    result='0'
while num>0:
    result=str(num%2)+result
    num//=2
if is_neg:
    result='-'+result
print(result)