# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:28:56 2019

@author: Maxwell
"""

def binarySearch(target, my_list):
    low=0
    high=len(my_list)
    mid=(low+high)//2
    while my_list[mid] != target:
        mid=(low+high)//2
        if target < my_list[mid]:
            high=mid-1
        elif target > my_list[mid]:
            low=mid+1
        else:
            return mid
        
samplelist = [0,1,2,3,4,5,6]

binarySearch(4, samplelist)
