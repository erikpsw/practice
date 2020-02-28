def bisect_search(l,e):
    def bisect_helper(l,e,low,high):
        if high==low:
            return l[low]==e
        mid=(high+low)//2
        if l[mid]==e:
            return True
            print(e + 'are in l' + mid)
        elif l[mid]>e:
            if low==mid:
                return False
            else:
                return bisect_helper(l,e,low,mid-1)
        else:
            return bisect_helper(l,e,mid+1,high)
    if len(l)==0:
        return False
    else:
        return bisect_helper(l,e,0,len(l)-1)

l1=[6,202,100,301,38,8,1]
bisect_search(l1,10)