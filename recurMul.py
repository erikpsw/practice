def recurMol(a,b):
    if b==1:
        return a
    else:
        return a+recurMul(a,b-1)
    
# b每次都减一，最后减到1，a相加的次数即为b次
# 递归思想
