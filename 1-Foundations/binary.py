from math import floor
def binary_search(input_array, target):
    #inputs: an array to perform the binary_search
    #an integer which is the num that we looking for
    # return -1 if it didn't find  or a dict {'result':guess,'count':count}
    count = 0;
    min = 0;
    max = len(input_array)-1;
    while max >= min:
        guess = floor((min+max)/2.0);
        count +=1
        if input_array[guess] == target:
            return {'result':guess,'count':count}
        elif input_array[guess]> target:
            max = guess -1
        elif input_array[guess]< target:
            min = guess +1
    return (-1,count)

#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
lower = 2
upper = 332

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

#print("Prime numbers between",lower,"and",upper,"are:")
primes= []
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num//2):
           if (num % i) == 0:
               break
       else:
           primes.append(num)

a,count = binary_search(primes ,52)
#print('the 53 is found in %i after %i quesses'%(a['result'],a['count']))
print('count = %i'%count)
