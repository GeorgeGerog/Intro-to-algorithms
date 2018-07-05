# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:10:03 2018

@author: user
"""

def selection_sort(A):
    #all in one function
    #input an array to sort
    #output a sorted array
    
    for i in range(len(A)):
        minValue = A[i]
        for j in range(i+1,len(A)):
            #find the smallest number
            if A[j] < minValue:
                minValue = A[j]
                minindex =j
        #swap the smallest number with the A[i]
        if minValue < A[i]:
            temp =A[i]
            A[i] =minValue
            A[minindex] = temp
    return A
#example
    
A= [5,9,7,1,6,-2]
#assert selection_sort(A)==[-2,1,5,6,7,9], 'not sorted right'

#or we can break it to more functions