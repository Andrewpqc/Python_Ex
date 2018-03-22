"""
二分查找
"""


def binary_search(list, item):
    """
    list:有序列表(从小到大排列)
    item:需要查找的元素
    """
    low = 0
    high = len(list) - 1

    while low < high:
        mid = (low + high) // 2
        if item == list[mid]:
            return mid
        elif item > list[mid]:  #查找值位于mid右边
            low = mid + 1
        else:
            high = mid - 1  #查找值位于mid左边
        return None  #没找到则返回None


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6]
    print(binary_search(l, 3))
    print(binary_search(l, 7))
