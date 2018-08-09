#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:01:01 2018

@author: pradyumna
"""
annualInterestRate=float(input("Enter the air"))
balance=int(input("Enter the balance"))
monthlyPaymentRate =float(input("enter the mpr"))
for i in range(12):
    Monthly_interest_rate=(annualInterestRate)/12.0
    Minimum_monthly_payment=monthlyPaymentRate *balance
    Monthly_unpaid_balance=balance-Minimum_monthly_payment
    
    Updated_balance=(Monthly_unpaid_balance)+(Monthly_interest_rate*Monthly_unpaid_balance)
    balance=Updated_balance
    print(round(Updated_balance,2))