# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:05:17 2020

@author: sandi
"""


# =============================================================================
# Mortgage class calculates the Mortgage yearly amount for an user
# =============================================================================
class Mortgage:
    '''
    # Mortgage Class calculates the mortgage amount needed to be paid by an user.
    # principle : The amount of Mortgage amount to be repaid.
    # mode   : The mode of repayment, values must be in ['m', 'q', 'h', 'y'] 
    #          for monthly, quarterly or half yearly, or yearly
    #          compounding of interest.
    # rate   : The interest rate.
    # years  : The number of years within which amount needs to be paid.
    
    '''

    def __init__(self, principle, mode, rate, years):
        self.principle = principle
        self.mode_val = Mortgage.repayment_mode(mode)
        self.rate = rate / 100
        self.years = years

    def repayment_mode(mode):
        if mode == 'm':
            return 12
        if mode == 'q':
            return 4
        if mode == 'h':
            return 2
        if mode == 'y':
            return 1

    def showMonthlyPayment(self):
        val = self.years
        i = 1
        yearly_principle = self.principle / val
        interest = self.principle * ((1 + (self.rate / self.mode_val)) ** (self.mode_val * self.years)) - \
                   self.principle
        while (val):
            print("Net Payment for year %d is %.2lf" % (i, yearly_principle + interest))
            i += 1
            val -= 1
        print("\nNet Amount Paid for %.2f is %.2f" % (self.principle, self.principle + interest))


# =============================================================================
# User Program to use the mortgage class for calculatig yearly expenses
# =============================================================================

values = input("Enter principle, mode, rate, years: ").split()
principle, mode, rate, years = float(values[0]), values[1], float(values[2]), int(values[3])

CalcMortgage = Mortgage(principle, mode, rate, years)

CalcMortgage.showMonthlyPayment()
