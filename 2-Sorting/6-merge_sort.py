#takes in an array that has two sorted subarrays,
#from [p..q] and [q+1..r], and merges the array
def merge(array, p, q, r):
    lowHalf =array[p:q+1]
    highHalf=array[q+1:r+1]
    i ,j = 0 , 0;
    k=p;
#   Repeatedly compare the lowest untaken element in
#   lowHalf with the lowest untaken element in highHalf
#   and copy the lower of the two back into array
    while(i < len(lowHalf) and j < len(highHalf)):
        if (lowHalf[i] < highHalf[j]):
            array[k] =lowHalf[i];
            i +=1;
        else:
            array[k] = highHalf[j];
            j +=1;
        k +=1;
        
#    // Once one of lowHalf and highHalf has been fully copied
#    //  back into array, copy the remaining elements from the
#    //  other temporary array back into the array
    while (i <len(lowHalf)):
            array[k] = lowHalf[i];
            i +=1;
            k +=1;
     
    while (j<len(highHalf)):
            array[k] = highHalf[j];
            j +=1;
            k +=1;
#Takes in an array and recursively merge sorts it
def mergeSort(array, p, r) :
    if (r-p>=1):
      q = (p+r)//2
      mergeSort(array,p,q);
      mergeSort(array,q+1,r);
      merge(array,p,q,r);
      

def main():
    array =[150,5,-15,12,0,9]
    print('Array before sorting '+str(array))
    mergeSort(array,0, len(array)-1)
    print('Array before sorting '+str(array))
main()
    
