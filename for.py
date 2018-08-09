#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:51:06 2018

@author: pradyumna
"""

mySum=0
for i in range(5):
    mySum+=i
print(mySum)
print("**********")




mySum=0
for i in range(5):
    mySum+=i
    print(mySum)
print("*****")



mySum=0
for i in range(5,7):
    mySum+=i
print(mySum)
print("************")



mysum=0
for k in range(5,11,2):
    mysum+=k
print(mysum)
print("************")


mysum=0
for i in range(5,11,2):
    mysum+=i
    if mysum==5:
        break
print(mysum)