# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:19:52 2020

@author: sandip
"""

# =============================================================================
# Function to implement Bubble Sort
# Runs in O(n^2) time
# =============================================================================

values = [2,10,1,0,7,7,8,9,4]

def Bubble_Sort(values):
    l = len(values)
    for i in range(0, l):
        for j in range(0, l - i - 1 ):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values
            
print(Bubble_Sort(values))

# =============================================================================
# Function to implement Merge Sort
# Runs in O(n.log n) time
# =============================================================================

def Merge(arr1, left, middle, right):
    l1 = middle - left + 1
    l2 = right - middle
    
    arr_l = arr1[left: middle + 1]
    arr_r = arr1[ middle + 1: right + 1]
    
    i, j, m = 0, 0, left
    
    while i < l1 and j < l2:
        if arr_l[i] < arr_r[j]:
            arr1[m] = arr_l[i]
            i += 1
        else:
            arr1[m] = arr_r[j]
            j += 1
        m += 1
        
    while i < l1:
        arr1[m] = arr_l[i]
        i += 1
        m += 1
        
    while j < l2:
        arr1[m] = arr_r[j]
        j += 1
        m += 1
    
    return arr1

def Merge_Sort(arr1, left, right):
    if left < right:
        middle = (left + (right - 1)) // 2
        Merge_Sort(arr1, left, middle)
        Merge_Sort(arr1, middle+1, right)
        Merge(arr1, left, middle, right)

val = [0, 9, 9, 1, 3, 7, 6]
Merge_Sort(val, 0, 6)
print(val)
    
        