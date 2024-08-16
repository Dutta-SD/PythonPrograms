# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:46:38 2020

@author: sandip
"""
# -----------------------------------------------------------------------------

# Python Code to Comupute the Value of PI upto required decimal places
# Used Chudnovsky Algorithm to compute the value
# Time Complexity = O(n * (logn)^3 )

import decimal


def pi_upto_k_places():
    # K is the number of decimal places

    k = int(input("Enter how many digits do you want? "))

    # Set precision a little more than needed

    decimal.getcontext().prec = k + 2

    # Constant for Multiplication
    C = decimal.Decimal(426880) * decimal.Decimal(10005).sqrt()

    Mk = decimal.Decimal(1)  # Multinomial Coefficient
    Xk = decimal.Decimal(1)  # Exponential Coefficient
    Lk = decimal.Decimal(13591409)  # Linear Coefficient
    Kk = decimal.Decimal(6)  # To compute Mk faster

    sum = decimal.Decimal(0)  # Stores the Sum

    # Computation by Algorithm, Loop Starts at O
    for i in range(0, k):
        sum += decimal.Decimal(Mk * Lk) / Xk
        Lk += 545140134
        Xk *= decimal.Decimal((-262537412640768000))
        Mk *= (Kk ** 3 - 16 * Kk) / decimal.Decimal(((i + 1) ** 3))
        Kk += 12

    return k, C / sum


decimal.getcontext().prec, PI = pi_upto_k_places()

# Precision from function is sticking and is not removing
# This issue needs to be taken care of

print(PI)
