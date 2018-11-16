# coding=utf-8

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。

def find_insert(alist, target):  # alist is a sorted list without duplicate elements
    if alist is None:
        return None

    # 二分法  O(log2n) 以2为底，n的对数
    i = 0
    j = len(alist)-1
    while i < j:
        mid = (i+j) / 2
        # print('i, j, mid: ', i, j, mid)

        if alist[mid] == target:
            return mid

        elif alist[mid] < target:
            if target < alist[mid+1]:
                return mid+1
            else:
                i = mid+1

        else:
            if target > alist[mid-1]:
                return mid    # attention here
            else:
                j = mid-1


    if i == j:   # 边界问题
        if target > alist[i]:
            return i+1
        else:
            return i     # attention here

# O(n)
def better_sol(alist, target):
    if alist is None:
        return None

    # 边界问题
    if target >= alist[-1]:
        return len(alist)
    if target <= alist[0]:
        return 0

    for i in range(len(alist)):   # loop over alist
        if alist[i] == target:
            return i
        if target not in alist:  # 当target没在nums中
            if target > alist[i] and target < alist[i + 1]:
                return i + 1


if __name__ == '__main__':
    alist = [2, 3, 4, 6, 7, 9, 12]
    # print(find_insert(alist, target=6))
    # print(find_insert(alist, target=8))
    # print(find_insert(alist, target=13))    # 边界问题
    # print(find_insert(alist, target=0))     # 边界问题

    print(better_sol(alist, 6))
    print(better_sol(alist, 8))
    print(better_sol(alist, 13))
    print(better_sol(alist, 0))