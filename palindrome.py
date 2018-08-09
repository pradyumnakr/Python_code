#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:28:37 2018

@author: pradyumna
"""

def toChars(s):
    s=s.lower();
    ans=''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans+=c
    return ans
def ispal(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and ispal(s[1:-1])
print(ispal(toChars("Prarp")))
