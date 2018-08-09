#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:13:21 2018

@author: pradyumna
"""

def fun(balance, annualInterestRate):    
    fixedPay =10
    monthlyInterest = annualInterestRate / 12
    debt = balance # use a initial variable to store start input balue
    # and keep refresh debt value every time
    while debt > 0:
        debt = balance # replace debt value after inner for loop       
        for i in range(12): # use two layer loop to control 
            debt -= fixedPay
            if debt <= 0: # set a condition to return fixedPay value
                return fixedPay 
            debt *= (monthlyInterest + 1)
##            print 'month :' + str(i)
##            print 'monthly payment: ' + str(fixedPay)
##            print 'debt :' + str(debt)
##            print '\n'
        fixedPay += 10 #test condition to continue
    
print (fun(4773, .2))