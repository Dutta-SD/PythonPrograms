# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:09:54 2020

@author: sandip
"""
#-----------------------------------------------------------------------------
#Python Program to print the value of e for k decimal places by euler formula

#e = 1 + 1/1! + 1/2! + 1/3! + 1/4! +...

import decimal as dc
from math import factorial as fact

def E_upto_k_places():
    
    k = int(input("Enter the precision: "))
    
    #Set the precision to one place more than is required
    
    dc.getcontext().prec = k + 1
    
    #Loop to add the terms 1 / x!
    
    sum = dc.Decimal(1)
    
    for i in range(1, k+1):
        sum += 1 / dc.Decimal(fact(i))
    
    return sum

print(E_upto_k_places())