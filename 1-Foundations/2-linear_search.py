# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:48:51 2018

@author: user
"""

#linear search O(n)
def linearsearch(array, target):
    
    for i in range(len(array)):
        if array[i] == target:
            return i
        
    return -1

array = [i**2 for i in range(15)]
result =linearsearch(array, 25)
if result == -1:
    print('The target was not in the array')
else:
    print('The target was found in the index %i '%result)