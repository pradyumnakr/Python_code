#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:16:45 2018

@author: pradyumna
"""

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n]=ans
        return ans

d={0:1,1:1}
print(fib_efficient(6,d))
print(d)