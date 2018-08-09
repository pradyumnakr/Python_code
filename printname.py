#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:42:49 2018

@author: pradyumna
"""

def printname(first,last,reverse=False):
    if reverse:
        print(last,first)
    else:
        print(first+" "+last)
printname("pradyumna","hebbar")