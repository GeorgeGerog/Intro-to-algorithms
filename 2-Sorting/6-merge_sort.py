#takes in an array that has two sorted subarrays,
#from [p..q] and [q+1..r], and merges the array
def merge(array, p, q, r):

    lowHalf =array[p:q+1]
    print('low array :' +str(lowHalf))
    highHalf=array[q+1:r+1]
    print('high array :' +str(highHalf))
    i ,j = 0 , 0;
    k=p;
#   Repeatedly compare the lowest untaken element in
#   lowHalf with the lowest untaken element in highHalf
#   and copy the lower of the two back into array
    while(i < len(lowHalf) and j < len(highHalf)):
        if (lowHalf[i] < highHalf[j]):
            array[k] =lowHalf[i];
            print('copy from low to array the %i '%(lowHalf[i]))
            i +=1;
            print('increasing i = %i'%i)

        else:
            array[k] = highHalf[j];
            print('copy from high to array the %i '%(highHalf[j]))
            j +=1;
            print('increasing j = %i'%j)

        k +=1;
        print('increasing k = %i'%k)
    print('array = '+str(array))
        
#    // Once one of lowHalf and highHalf has been fully copied
#    //  back into array, copy the remaining elements from the
#    //  other temporary array back into the array
    while (i <len(lowHalf)):
            array[k] = lowHalf[i];
            print('coping the remaing num from low %i'%lowHalf[i] )
            i +=1;
            k +=1;
     
    while (j<len(highHalf)):
            array[k] = highHalf[j];
            print('coping the remaing num from high %i'%highHalf[j] )
            j +=1;
            k +=1;
    print('array = '+str(array))
     





#Takes in an array and recursively merge sorts it
def mergeSort(array, p, r) :
    if (r-p>=1):
      q = (p+r)//2
      print('q= %i'%q)
      print('calling sort low before:')
      mergeSort(array,p,q);
      print('calling sort low after  p =%i q =%i:'%(p,q))
      print('calling sort high before:')
      mergeSort(array,q+1,r);
      print('calling sort high after q+1 =%i r =%i:'%(q+1,r))
      print('calling sort merge before: p =%i q =%i r=%i:'%(p,q,r))
      merge(array,p,q,r);
      print('calling sort merge after:')
      


array = [2,1,7,3,-4];
print("Array before sorting: " + str(array));
mergeSort(array, 0, len(array)-1);
print("Array after sorting: " + str(array));
#assert array ==[2, 3, 6, 7, 9, 11, 12, 14], 'Not sorted correct';
