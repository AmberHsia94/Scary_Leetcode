# coding=utf-8

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#

# 给定的数组是排序数组；
# 循环数组，找到下一个元素A[i + 1]等于A[i]，就删除A[i + 1]，
# 注意的是循环次数需要 - 1，避免索引超限。
#
# 允许重复一次，则直接检查元素A[i + 2]
# 是否等于A[i]即可，因为如果A[i + 2]等于A[i]，那么A[i + 1]也等于A[i]，
# 此时删除A[i + 2]即可。 当然，循环次数需要 - 2

def delete_dup(alist):  # alist is a sorted list
    if alist is None:
        return 'Empty list.'

    print alist
    i = 1
    while i < len(alist):
        # print i
        if alist[i] == alist[i-1]:
            alist.remove(alist[i])  # delete ALL duplicate elements in THIS Loop
        else:  # going forward
            i = i + 1
        print alist



def delete_dup2(alist):   # alist is a sorted list
    if alist is None:
        return 'Empty list.'
    print alist

    i = 2
    while i < len(alist):
        if alist[i] == alist[i-2]:
            alist.remove(alist[i])
        else:
            i = i+2
        print alist


if __name__ == '__main__':
    alist = [1,1,1,4,5,5,6,9]
    # delete_dup(alist)
    delete_dup2(alist)
