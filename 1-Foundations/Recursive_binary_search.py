# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:58:49 2018

@author: George Gerog
"""
#recursive relation
#T(n) = 1 if n=1
#T(n) =T(n/2) + c if n>1  Θ(logn)
def RBinSearch(array, l, r, key):
    #takes as input a sorted array, l =left index, r = right indes
    #key = target
    #return the index of key, if not found returns -1
    if l==r:
        if array[l]==key:
            print("Target %i is found at index : %i"%(key,l))
            return l
        else:
            print('Target %i not found.'%key)
            return -1
    else:
        mid =(l+r)//2
        if key == array[mid]:
            print("Target %i is found in index : %i"%(key,mid))
            return mid
        if key < array[mid]:
            return RBinSearch(array, l, mid-1 ,key)
        else:
            return RBinSearch(array,mid +1 ,r, key)
def main():
    array = [-2,0,1,3,15]
    RBinSearch(array,0, len(array)-1, 15)
main()
            
