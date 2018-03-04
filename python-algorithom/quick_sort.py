def quick_sort(l):
    """
    对l进行快速排序
    """
    if len(l)<2:
        return l
    else:
        povit=l[0]
        less=[i for i in l[1:] if i<=povit]
        greater=[j for j in l[1:] if j>povit]
        return quick_sort(less)+[povit]+quick_sort(greater)
    
if __name__=="__main__":
    l=[1,5,0,3,2,4,6,9]
    print(quick_sort(l))