# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 21:19:07 2018

@author: George Gerog
"""
from random import randint
#Swaps two items in an array, changing the original array
def swap(array, firstIndex, secondIndex): 
    array[firstIndex], array[secondIndex] =array[secondIndex], array[firstIndex]
    
def partition(array, p, r):
    j =p;
    q =p;
    for j in range(p,r,1):
        if(array[j] <= array[r]):
            swap(array,j,q);
            q =q+1;
    swap(array, r,q);
    return q;


def randomizedPartition(array, p, r):
    i = randint(p, r)
    swap(array,r ,i)
    return partition(array, p, r)

def quickSort(array, p, r): 
    if (p <r):
        q = randomizedPartition(array, p ,r);
        quickSort(array, p, q -1);
        quickSort(array, q +1, r);
        
def main():
    array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
    quickSort(array, 0, len(array)-1);
    print("Array after sorting: " + str(array));
    assert array == [2,3,5,6,7,9,10,11,12,14], 'list not correct sorted'
    
    array = [0,-2,15,-4,19];
    quickSort(array, 0, len(array)-1);
    print("Array after sorting: " + str(array));
    assert array == [-4,-2,0,15,19], 'list not correct sorted'
    
main()