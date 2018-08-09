#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:36:26 2018

@author: pradyumna
"""
import pylab as plt
mySamples=[]
myLinear=[]
myQuadratic=[]
mycubic=[]
myExponential=[]
for i  in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    mycubic.append(i**3)

plt.plot(mySamples,mycubic)