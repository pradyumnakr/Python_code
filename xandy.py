#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:39:51 2018

@author: pradyumna
"""

x=float(input("Enter the number for x\n"))
y=float(input('Enter the number for y\n'))
if x==y:
    print("x and y are equal")
    if y!=0:
        print("therefore x/y is",x/y)
elif x<y:
    print("x is smaller")
else:
    print("y is smaller")
print('thnaks')