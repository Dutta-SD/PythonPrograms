# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:41:49 2020

@author: sandip
"""


# =============================================================================
# Algorithm for fast exponentiation (Binary Exponentiation)
# Exponentiation in O( log n ) time
# =============================================================================

def Bin_Expo(a, n):
    # if the exponent is 0, return 1(Base Case)
    if n == 0:
        return 1
    if n & 1:
        # If the exponent is odd ,then call Bin_Expo with (a^(n-1)/2)**2 * a
        return Bin_Expo(a, (n - 1) >> 1) * Bin_Expo(a, (n - 1) >> 1) * a
    # Call the Bin_Expo with (a^(n/2))*2
    return Bin_Expo(a, n >> 1) * Bin_Expo(a, n >> 1)


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


# =============================================================================
# Driver Functions
# =============================================================================

print(Bin_Expo(3, 20))
print(GCD(10, 5))
