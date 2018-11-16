# -*- coding:utf-8 -*-
#  searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 比较最右元素
        row = 0
        col = len(array[0])-1
        while row < len(array) and col >= 0:
            right = array[row][col]
            print(right)
            if target == right:
                return True
                break
            elif target > right:
                row += 1
            else:
                col -= 1


k = 1
n = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
sol = Solution()

print(sol.Find(k,n))