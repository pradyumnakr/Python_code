#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:40:25 2018

@author: pradyumna
"""

x=25
ans=0
intersleft=x
while(intersleft!=0):
    ans+=x
    intersleft-=1
print(str(x) +"*" +str(x)+"="+str(ans))