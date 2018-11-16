# -*- coding:utf-8 -*-
# 翻转数组中的最小值 [4, 5, 1, 2, 3]

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        start = 0
        end = len(rotateArray) - 1

        while rotateArray[start] >= rotateArray[end]:
            # print('start: ', rotateArray[start])
            # print('end: ', rotateArray[end])
            mid = (start + end) / 2
            # print('mid: ', rotateArray[mid])

            if end - start == 1: # only two elements
                return rotateArray[end]
                break

            # equal elements
            if rotateArray[start] == rotateArray[mid] and rotateArray[mid] == rotateArray[end]:
                return rotateArray[mid]
                break

            if rotateArray[mid] > rotateArray[end]:
                start = mid
            if rotateArray[mid] < rotateArray[start]:
                end = mid



sol = Solution()
print(sol.minNumberInRotateArray([4, 5, 1, 2, 3]))
print(sol.minNumberInRotateArray([4, 6, 7, 2, 3]))
print(sol.minNumberInRotateArray([2, 2, 1, 2, 2]))



