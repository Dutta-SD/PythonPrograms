#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program to implement QuickSort
# For random indexing
from random import randint

# Randomized Quicksort
def QuickSort(val, start, end):
    # Base Case, start > end means empty array, so return
    if start > end:
        return
    
    # Select a random index for Pivoting
    pivot_index = randint(start, end)
    # Swap Pivot with starting element
    val[pivot_index], val[start] = val[start], val[pivot_index]    
    
    # Starting point of the pointers
    # array from start+1 to less_ptr-1 is less than pivot
    # Array from less_ptr to more_ptr is greater than pivot
    # Array from more_ptr to end is unknown 
    less_ptr = more_ptr = start + 1    
    
    # Move more_ptr, if see any element less than pivot, swap
    # with less pointer position
    for more_ptr in range(start + 1, end + 1):
        if val[more_ptr] < val[start]:
            val[more_ptr], val[less_ptr] = val[less_ptr], val[more_ptr]
            #Increase less pointer by 1 for further swaps
            less_ptr += 1
    # Put pivot in correct position      
    val[start], val[less_ptr - 1] = val[less_ptr - 1], val[start]
    
    # QuickSort on the remaining portions
    QuickSort(val, start, less_ptr - 2)
    QuickSort(val, less_ptr, end)
    # As this is inplace operation, we do not return anything


val = [randint(-1000, 1000) for x in range(0, 1000)]
QuickSort(val, 0, 999)
print(val)

#_____________________________________________________________________________

# Now that we have a sorted array, let us look for a value using 
# Binary Search

def BinSearch(val, start, end, value):
    # Base Case
    if start > end:
        return False
    
    # mid is the middle position
    mid = (start + end) // 2
    
    if value == val[mid]:
        return mid
    elif value > val[mid]:
        return BinSearch(val, mid+1, end, value)
    else:
        return BinSearch(val, start, mid - 1, value)
    
    
print(BinSearch(val, 0, 999, -1000))
#___________________________________________________________________________________
# NOTE: Since we have not inserted random.seed we will get different results for
# Different times
    



    
        
    