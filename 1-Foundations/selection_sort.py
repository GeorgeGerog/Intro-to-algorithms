# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:05:47 2018

@author: George Gerog
"""
def indexOfMinimum(array, startIndex):
    minValue =array[startIndex]
    minIndex = startIndex
    
    for i in range(startIndex + 1, len(array)):
        if array[i] < minValue:
            minIndex = i
            minValue = array[i]
    return minIndex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] =array[secondIndex]
    array[secondIndex] = temp
    
    
def selection_sort(array):
    for i in range(len(array)):
        index = indexOfMinimum(array,i );
        swap(array,i,index);
    

def main():
    a= [0,-2,-8,15,50,1]
    selection_sort(a)
    print(a)
main()


            
            