# coding=utf-8
# Longest Increasing Subsequence
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4]
# 给定一个长度为N的数组，找出一个最长的单调自增子序列（不一定连续，但是顺序不能乱）。
# 例如：给定一个长度为6的数组A{5，6，7，1，2，8}，则其最长的单调递增子序列为{5，6，7，8}，长度为4.


# 第一个元素不一定会用！！


# 1. 动态规划
# O(n*n)
# [10, 2, 11, 4, 12, 6, 1] --- [2, 4, 6]
# condition: 找到当前元素的最长递增子序列， 必须找到所有结尾元素都在当前元素（eg: 6）左边
#            并且结尾元素比6小的最长递增子序列
# https://segmentfault.com/a/1190000012748540

def max_ascend(alist):
    max_len_at_i = {}

    for i in range(len(alist)):
        max_len_at_i[i] = 1   # intialization
        for j in range(i):
            if alist[j] < alist[i]:
                if max_len_at_i[i] < max_len_at_i[j] + 1:
                    max_len_at_i[i] = max_len_at_i[j] + 1

    print max_len_at_i

    return max(max_len_at_i.items())[1]


# 2. O(nlogn)
# 维护一个tail数组，代表几元数组最小元素的数值， 通过二分查找找插入点， 最大长度＝tail数组的长度
# http://blog.csdn.net/u012505432/article/details/52228945
def lis(alist):
    tails = []
    if not tails:
        tails.append(alist[0])

    for i in range(len(alist)):
        if alist[i] > tails[-1]:
            tails.append(alist[i])
        else:
            rep = bisearch(tails, alist[i])
            tails[rep] = alist[i]

    print tails
    return len(tails)


def bisearch(alist, num):
    first = 0
    end = len(alist) - 1

    while first < end:
        mid = first + (end - first)/2
        print('mid: ', mid)
        if alist[mid] == num:
            return num
        elif alist[mid] < num:
            first = mid + 1
        else:
            end = mid - 1

    return first


# 转换为最长公共子序列问题。
# 如例子中的数组A{5，6， 7， 1， 2， 8}，则我们排序该数组得到数组A‘{1， 2， 5， 6， 7， 8}，然后找出数组A和A’的最长公共子序列即可。
# 显然这里最长公共子序列为{5, 6, 7, 8}，也就是原数组A最长递增子序列




if __name__ == '__main__':
    alist = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    print max_ascend(alist)

    # print bisearch([2, 7, 10, 15], 8)
    # print lis(alist)
