#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:45:15 2018

@author: pradyumna
"""

ans =0
neg_flag=False
x=int(input("Enter an integer:"))
if x<0:
    neg_flag=True
while ans**2<x:
    ans+=1
if ans**2==x:
    print("Square root of ",x,"is" ,ans)
else:
    print(x,"is not a perfect square")
    if neg_flag:
        print("just checking...did you mean", -x,"?")
    