# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:14:39 2018

@author: Georgre Gerog
"""
def binary_add(A,B):
    #input two arrays with a n-bit integers each
    #output an array with the sum of the integers (n+1)bit
    C = [0 for _ in range(len(A) +1 )]
    carry =0
    for i in range(len(A)-1,-1,-1):
        C[i+1] =(A[i]+B[i]+carry)%2
        carry = (A[i] +B[i] +carry)//2
    return C

#example
a = [1,0,1]
b = [1,1,0]
c = binary_add(a,b)
print('The result is '+ str(c))