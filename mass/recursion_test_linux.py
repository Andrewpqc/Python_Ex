"""
python解释器直接识别出这是一
个没有终止条件的递归函数，不予执行
"""
def recursion(i):
    print(i)
    recursion(i+1)

if __name__ == '__main__':
    recursion(1)