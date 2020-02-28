def issubset(l1,l2):
    for e1 in l1:
        matched=False
        for e2 in l2:
            if e2==e2:
                matched=True
                break
            if not matched:
                return False
    return True

l1=[1,2,35,1,5,1425,45,4,58,51,8,2514,58,561,5]
l2=[5,4,86,14,581,581,5841,351,4,6841,651,568,4]

issubset(l1,l2)
