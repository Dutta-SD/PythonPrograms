# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:24:32 2020

@author: sandi
"""

# =============================================================================
# Collantz Conjecture : If n is even, divide by 2
# If it is odd, multiply by 3 and add 1 
# =============================================================================

n = int(input("Enter a number: "))
count = 0
while(n != 1):
    if n & 1:
        n = 3 * n + 1
        count += 1
    else:
        n = n // 2
        count += 1

print(count)

        