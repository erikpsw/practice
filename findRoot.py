print('findRoot(,,)')
def findRoot(x,power,epsilon):
    if x<0 and power%2==0:
        return None
    low=min(-1,x)
    high=max(1,x)
    ans=(high+low)/2
    while abs(ans**power-x)>epsilon:
        if ans**power<x:
            low=ans
        elif ans**power>x:
            high=ans
        ans=(high+low)/2
        print('current_root='+str(ans))
    return ans
