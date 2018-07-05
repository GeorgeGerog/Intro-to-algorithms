# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:15:46 2018

@author: George Gerog
"""

def insertion_sort(array, increasing = True):
    if increasing == True:
        #input an array to be sorted
        #output a sorted array increasing order
        for j in range(1,len(array)):
            key = array[j]
            # Insert A[j]  into the sorted sequence A[0...j-1]
            i = j-1
            while i>=0 and array[i] > key:
                array[i+1]= array[i]
                i =i-1
            array[i+1] =key
        return array
    else:
        #input an array to be sorted
        #output a sorted array non increasing order
        for j in range(1,len(array)):
            key = array[j]
            # Insert A[j]  into the sorted sequence A[0...j-1]
            i = j-1
            while i>=0 and array[i] < key:
                array[i+1]= array[i]
                i =i-1
            array[i+1] =key
        return array
        
array =[31,41,59,26,41,58]
result = insertion_sort(array, False)
print('The sorted list is  '+str(result))


             