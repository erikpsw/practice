while True:
    elpsilon=0.01
    y=int(input('number='))
    guess=y/2
    while abs(guess**2-y>=elpsilon):
        guess=guess-((guess**2-y)/(2*guess))
        print(guess)
    print('square root of'+str(y)+'is about'+str(guess)) 
            
        
        
