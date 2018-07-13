# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:28:58 2018

@author: George Gerog
"""

#Swaps two items in an array, changing the original array
def swap(array, firstIndex, secondIndex): 
    temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;


def partition(array, p, r):
#    // Compare array[j] with array[r], for j = p, p+1,...r-1
#    // maintaining that:
#    //  array[p..q-1] are values known to be <= to array[r]
#    //  array[q..j-1] are values known to be > array[r]
#    //  array[j..r-1] haven't been compared with array[r]
#    // If array[j] > array[r], just increment j.
#    // If array[j] <= array[r], swap array[j] with array[q],
#    //   increment q, and increment j. 
#    // Once all elements in array[p..r-1]
#    //  have been compared with array[r],
#    //  swap array[r] with array[q], and return q.
    j =p;
    q =p;
    for j in range(p,r,1):
        if(array[j] <= array[r]):
            swap(array,j,q);
            q =q+1;
    swap(array, r,q);
    return q;

def quickSort(array, p, r): 
    if (p <r):
        q = partition(array, p ,r);
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