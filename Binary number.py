while True:
    num=int(input('num'))
    result=str(" ")
    while num>1:
        result=str(num%2) + result
        num=num//2
    print(result)
    
