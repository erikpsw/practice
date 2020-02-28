def fib(x):
    global numCalls
    numCalls=0
    numCalls+=1
    assert type(x)==int and x>=0
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
    print(numCalls)
