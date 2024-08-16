# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:33:20 2020

@author: sandip
"""


# =============================================================================
# To solve the closest pair problem in O(nlogn) time. 
# We sort the points along x coordinate and then sort by y coordinate.
# Then we get 4 points. We then obtain the minimum distance between these four
# points and give the answer. To do that we would need the merge sort procedure
# =============================================================================

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2  # Euclidean Distance squared


# =============================================================================
# Merge Procedure is the normal merge sort procedure except that it has a flag
# parameter. It decides on the basis of which coordinate we will sort the 
# points. 0 for x values, 1 for y values.
# =============================================================================

def Merge(arr1, left, middle, right, flag):
    l1 = middle - left + 1
    l2 = right - middle

    arr_l = arr1[left: middle + 1]
    arr_r = arr1[middle + 1: right + 1]

    i, j, m = 0, 0, left

    while i < l1 and j < l2:
        # tuple.__getitem__(index) returns the item at index
        if arr_l[i].__getitem__(flag) < arr_r[j].__getitem__(flag):
            arr1[m] = arr_l[i]
            i += 1
        else:
            arr1[m] = arr_r[j]
            j += 1
        m += 1

    # If the array is not filled, then these steps take place
    while i < l1:
        arr1[m] = arr_l[i]
        i += 1
        m += 1

    while j < l2:
        arr1[m] = arr_r[j]
        j += 1
        m += 1


def Merge_Sort(arr1, left, right, flag):
    if left < right:
        middle = (left + (right - 1)) // 2
        Merge_Sort(arr1, left, middle, flag)
        Merge_Sort(arr1, middle + 1, right, flag)
        Merge(arr1, left, middle, right, flag)


# =============================================================================
# Closest Pair gets the 2 closest points based on x values. For 1D case 
# just comparing the x values will suffice. In this driver code only integer
# valued points are taken. For float values, we need to change the code.
# =============================================================================

def Closest_Pair(points, left, right):
    closest_points = []
    # sort by x values
    Merge_Sort(points, left, right, 0)
    closest_points.extend([points[0], points[1]])

    # sort by y values
    Merge_Sort(points, left, right, 1)
    closest_points.extend([points[0], points[1]])

    # Calculate the minimum distance between two points    
    minimum = dist(closest_points[0], closest_points[1])

    for i in range(0, 3):
        for j in range(i + 1, 4):
            val = dist(closest_points[i], closest_points[j])
            print("Distance squared between {0} and {1} is: {2}".format(
                closest_points[i], closest_points[j], val))
            if val < minimum:
                minimum = val

    print("The minimum distance is ", minimum)


# =============================================================================
# driver code to test the program
# =============================================================================

points = [(2, 3), (1, 7), (3, 9), (8, 0), (9, 9), (10, 1), (6, 2), (8, 5), (1, 4)]
Closest_Pair(points, 0, 8)
