def selection_sort(l):
    suffixst=0
    while suffixst <len(l):   #对0~len(l）的元素进行比较
        for i in range(suffixst,len(l)):
            if l[i]<l[suffixst]:
                l[suffixst],l[i]=l[i],l[suffixst]
                print(l[suffixst])
        suffixst+=1
l1=[6,202,100,301,38,8,1]
selection_sort(l1)
print(l1)


