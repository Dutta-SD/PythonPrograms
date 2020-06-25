#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Statistics exploration using SciPy'''
''' Few tests, Linear Regression, and Distributions explored here,
along with proper explanations'''


'''
1. Shapiro-Wilk test: This test is useful for testing if a data sample
has a Gaussian Distribution or not.
'''
import numpy
from scipy.stats import shapiro

samples = numpy.array([0.873, 2.817, 0.121,
                       -0.945, -0.055, -1.436,
                       0.360, -1.478, -1.637, -1.869])

# p value for shapiro test detected
value, p_value = shapiro(samples)

# Testing if p_value is significant or not
if p_value > 0.05:
    print('Likely gaussian with 95% confidence')
else:
    print('Unlikely to be Gaussain')


'''
2. Pearson Correlation Coefficient: Checks whether two data samples have
linear correlation or not. 
'''
from scipy.stats import pearsonr

samples_2 = numpy.array([ 0.991, 3.150, 0.212,
                          -0.799, -0.055, -1.002,
                          0.443, -1.0, -1.44, -2.21])
    
#Testing if p_value is signnificant or not
corr_coef, p_value = pearsonr(samples, samples_2)

if p_value > 0.05:
    print('Likely to be linearly correleated')
else:
    print('Unlikely to be correlated')
    
    
'''
3.  Spearman rank correlation: Checks if two samples have monotonic
relationship or not'''

from scipy.stats import spearmanr

stat, p_value = spearmanr(samples, samples_2)
if p_value > 0.05:
    print('Likely to be correlated via spearman test')
else:
    print('Unlikely to be correlated')
    


    
    


