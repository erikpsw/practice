def Nth_power(x,n):
    result=1
    for turn in range(n):
        print('iteration:'+str(turn)+'current_result:'+str(result))
        #iteration:迭代，current:当前
        result=result*x
    return result

