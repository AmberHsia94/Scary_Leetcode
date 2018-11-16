# coding=utf-8
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# https://leetcode-cn.com/problems/pascals-triangle/description/

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def method(n):
    if n is None:
        return

    if n==1:
        return [1]

    if n==2:
        return [[1],[1,1]]

    nums = [[1],[1,1]]   # key points
    for i in range(2,n):
        nums.append([1])
        for j in range(1,i):
            nums[i].append(nums[i-1][j-1]+nums[i-1][j])
        nums[i].append(1)
    print nums


method(n=5)

