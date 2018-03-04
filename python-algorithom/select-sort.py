"""
选择排序
"""


def selectSmallest(arr):
    """
    找出arr中的最小值，及其对应的索引，并返回
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index, smallest


def select_sort(arr):
    """
    选择排序，返回排序后的结果
    """
    newArr = []
    for i in range(len(arr)):
        smallest_index, smallest = selectSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == "__main__":
    l = [2, 1, 5, 0, 6, 9]
    l2 = select_sort(l)
    print(l2)
