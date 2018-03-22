def sum_recursive(l):
    """
    递归计算列表的元素之和
    """
    if len(l)==1:
        return l[0]
    else:
         return l[0]+sum_recursive(l[1:])



def counter_recursive(l):
    """
    递归统计列表的元素个数
    """
    if len(l)==1:
        return 1
    else:
        return 1+counter_recursive(l[1:])


def max_recursive(l):
    """
    递归计算列表中的最大值
    """
    if len(l)==1:
        return l[0]
    else:
        

if __name__=="__main__":
    l=[1,2,3]
    print("sum:",sum_recursive(l))
    print("counter:",counter_recursive(l))
