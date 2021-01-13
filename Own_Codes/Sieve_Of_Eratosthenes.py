# -*- coding: utf-8 -*-

# =============================================================================
# Sieve of Eratosthenes : To find all primes using sieve of Eratosthenes
# =============================================================================

def Sieve_of_Eratosthenes(n):
    arr = list(range(0, n+1))
    p = 2
    while(p <= n):
        t = p * p
        while t <= n:
            arr[t] = -1
            t += p
        p = p+1
        while p <= n+1:
            if p != -1:
                break
            p += 1         
    return arr
    

# =============================================================================
# Driver Function to test the function
# =============================================================================
    
val = Sieve_of_Eratosthenes(200)
print([i for i in val[2:] if i != -1])
            
    
             
             
