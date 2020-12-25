# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:09:03 2020

@author: sandip
"""

''' To implement Fraction class
For simplicity we have taken all values of fractions to 
be integers'''

class Fraction:
    def __init__(self, numR = 0, denR = 1):
        ''' represents fractions as a / b form. Each Fraction has 
        two parts, a which is numerator and b is denominator
        We set default Fraction value to 0 / 1'''
        
        assert type(numR) == int and type(denR) == int,\
        "Integer arguments expected. Got numR {} , denR {} ".format(numR, denR)
        
        assert denR != 0, "Denominator Cannot be zero"
        
        self.numR = numR
        self.denR = denR
        
    def __repr__(self):
        ''' Represents Fraction type object'''
        
        return "Fraction(Numerator: {}, Denominator: {}) [{}/{}]".format(
                self.numR, self.denR, self.numR, self.denR)
    
    def __str__(self):
        ''' String representations of fractions'''
        
        return "{} / {}".format(self.numR, self.denR)
    
    def __add__(self, other):
        '''addition of two fractions'''
        
        frac = Fraction()
        frac.numR = self.numR * other.denR + self.denR * other.numR
        frac.denR = self.denR * self.numR
        
        return frac
    
    def __sub__(self, other):
        '''subtraction of two fractions'''
        
        frac = Fraction()
        frac.numR = self.numR * other.denR - self.denR * other.numR
        frac.denR = self.denR * self.numR
        
        return frac
    
    def __mul__(self, other):
        ''' multiplication of two fractions'''
        
        return Fraction(self.numR * other.numR, self.denR * other.denR )
    
    def __truediv__(self, other):
        '''Division for two fractions. 
        If numerator is zero, then raise exception'''
        
        if other.numR == 0:
            raise ZeroDivisionError
        return Fraction(self.numR * other.denR, self.denR * other.numR)
    
   
# Test Code to check the functioning
frac1 = Fraction(8, 9)
frac2 = Fraction(3, 4)

print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)
print(frac1.__repr__())

    
    
        
        
        
        
    
    
    
    
    
    
    