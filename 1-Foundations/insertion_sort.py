"""
Created on Fri Jul  6 11:15:46 2018

@author: George Gerog
"""
def insert(array, rightIndex, value):
    # insert the given value into the array
    j = rightIndex
    while (j>=0 and array[j] > value):
        array[j+1] = array[j]
        j -=1
    array[j+1]=value


def insertionSort(array):
    #call insert function for 1...len(array) values
    for i in range(1,len(array)):
        insert(array,i-1,array[i])



def main():
    #calls insertionSort and checks if the output is correct
    array = [22, 11, 99, 88, 9, 7, 42];
    insertionSort(array)
    print("Array1 after sorting:  " + str(array))
    assert array, [7, 9, 11, 22, 42, 88, 99]
    
    array = [22, 11, -99, 88, 9, 0, 42];
    insertionSort(array)
    print("Array2 after sorting:  " + str(array))
    assert array, [-99,0, 9, 11, 22, 42, 88, 99]
main()
