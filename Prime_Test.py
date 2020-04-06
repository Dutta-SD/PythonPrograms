# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 07:41:58 2020

@author: sandip
"""
# =============================================================================
# Checks if Number is prime or not. Runtime is O( n ** 0.5 )
# =============================================================================
def isPrime(n):
    i = 2
    while(i*i <= n):
        if n % i == 0:
            return False
        i += 1        
    return True


num = int(input("Enter a number: "))
# =============================================================================
# Prints out the prime factors of the number, starting from 2
# =============================================================================

for i in range(2, num + 1):
    if num % i == 0 and isPrime(i) == True :
        print(i)
        


