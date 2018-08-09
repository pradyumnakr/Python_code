#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:08:25 2018

@author: pradyumna
"""

def g(x):
    def h(x):
        x='abc'
    x=x+1
    print("In g(x):x ",x)
    h(3)
    return x
x=3
z=g(x)
print(z)   
  