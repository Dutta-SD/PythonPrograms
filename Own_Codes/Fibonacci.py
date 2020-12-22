# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:37:19 2020

@author: sandip
"""

#Program to generate fibonacci numbers upto n terms

n = int(input("Enter number of terms upto which displayed: "))
a0 = 0
a1 = 1
i = 1
while n:
    temp = a0
    a0 = a1
    a1 += temp
    print( "Term %d : %d " % (i, a0) )
    i += 1
    n -= 1

    