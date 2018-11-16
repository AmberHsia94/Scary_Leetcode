# coding=utf-8

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n))

# eg:
# nums1 = [1, 2], nums2 = [3, 4]
# 中位数是 (2 + 3)/2 = 2.5

# get_median([3, 6, 10, 15, 99]) == 12.5


# Hints:
# 如果列表数据的个数是奇数，则列表中间那个数据就是列表数据的中位数；
# 如果列表数据的个数是偶数，则列表中间那2个数据的算术平均值就是列表数据的中位数。

def two_medians(alist1, alist2):
    if alist1 is None and alist2 is None:
        return None

    # concatenate and sort first
    alist = sorted(alist1+alist2)  # quick-sort
    print alist

    # find median
    if len(alist)%2 == 0:    # 长度是偶数
        return (alist[len(alist)/2] + alist[len(alist)/2-1])/2
    else:
        return alist[len(alist)/2]



if __name__ == '__main__':
    alist1 = [1]
    alist2 = [3, 4]
    print(two_medians(alist1, alist2))