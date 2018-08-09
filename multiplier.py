#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:33:05 2018

@author: pradyumna
"""

def multiplier(a,b):
    result=0
    while(b>0):
        result+=a
        b-=1
    print(result)
multiplier(2,8)