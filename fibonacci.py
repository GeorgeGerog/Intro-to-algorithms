#the algorithm has an exponetial complexity
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#for i in range(0,100,20):
#    print('Fib(%i) = %i'%(i,fib(i)))

#the algorithm has linear complexity
def fib2(n):
    if n == 0:
        return 0
    f = [i for i in range(n+1)]
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] +f[i-2]
    return f[n]

for i in range(100:
    print('Fib(%i) = %i' % (i, fib2(i)))