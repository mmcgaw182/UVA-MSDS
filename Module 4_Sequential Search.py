# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:44:54 2019

@author: Maxwell
User ID: mm9tk
Binary Search Algorithm
"""

def binarySearch(target, my_list):
    mid=round(len(my_list)/2) #define initial midpoint
    if my_list[mid] == target:
        return 'yay!'
    elif my_list[mid]<target:
        newmid=round((mid-1)/2)
        if my_list[newmid] == target: #use binary search within formul definition?
            return 'yay!
    elif my_list
        