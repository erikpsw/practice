def bubble_sort(l):
    swap=False   #定义swap
    while not swap:
        swap=True
        for j in range(1,len(l)):
            if l[j-1]>l[j]:
                swap=False
                l[j-1],l[j]=l[j],l[j-1]
    return l

l1=[6,202,100,301,38,8,1]
bubble_sort(l1)
print(l1)
