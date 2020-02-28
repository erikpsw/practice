while True:
    x=int(input('number='))
    low=int(0)
    numGuesses=0
    high=x
    epsilon=0.01
    while numGuesses!=100:
        ans=(high+low)/2
        print('low='+str(low)+'high='+str(high)+'ans='+str(ans))
        numGuesses+=1
        if ans**2<x:
            low=ans
        elif ans==high:
            break
        elif ans==low:
            break
        else:
            high=ans
        ans=(high+low)/2
    print(str(numGuesses))
    print(str(ans)+'is close enough to the answer')
