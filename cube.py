#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:57:56 2018

@author: pradyumna
"""

x=int(input("enter an integer"))
ans=0
while(ans**3<x):
    ans+=1
if ans**3!=x:
    print(str(x)+ ' is not a perfect cube')
else:
    print(str(x)+ " cube is "+str(ans))
    