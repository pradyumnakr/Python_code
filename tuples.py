#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:10:03 2018

@author: pradyumna
"""

def qandr(x,y):
    q=x//y
    r=x%y
    return (q,r)
print(qandr(20,5))