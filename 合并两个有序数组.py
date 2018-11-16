# coding=utf-8
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

#
# 输入:
# nums1 = [1,2,3,0,0,0] m = 3
# nums2 = [2,5,6]       n = 3
#
# 输出: [1,2,2,3,5,6]


# 双指针，O(n)
# 从前往后，每插入一个数字， 整个数组往后挪动一位
# 所以对list_1从后往前插入

# 如果单纯从前往后合并，那么效率会非常低，因为a数组后面的数字需要不停的移动。换一种思路，我们采用从后往前合并，首先计算出总长度，设置一个指针从a数组最后往前移动。
def merge(alist1, alist2):
    len_a = len(alist1)  # 两指针
    len_b = len(alist2)

    while len_a > 0 and len_b > 0:
        if alist1[len_a-1] > alist2[len_b-1]:  # 列表皆有序，若nums1中最后一个元素大于nums2[]中最后一个元素
            alist1[len_a+len_b-1] = alist1[len_a-1]   # 则扩展后的alist1列表最后一个元素是俩元素中最大的
            len_a = len_a - 1
        else:
            alist1[len_a+len_b-1] = alist2[len_b-1]
            len_b = len_b - 1

        if len_b > 0:  # 若nums1完了，nums2还没完
            alist1[:len_b] = alist2[:len_b]  # 把剩下nums2加在最开始

if __name__ == '__main__':
    alist1 = [1,2,3]
    alist2 = [3,5,6]
