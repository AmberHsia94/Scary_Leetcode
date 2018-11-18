# coding=utf-8

# 从数组中是否存在数字的组合，使其的和为给定数值target。
# [3,34,4,12,5,2], target = 9, return T/F
#
# Recursion:
# 对于每个数，依旧是选 or 不选的关系。
#			选：寻找subset[i-1]的和 == target - value[i]
# 			不选： 寻找subset【i-1】的和 == target
#
# 停止条件：
# 		如果 s = 0： 不用再去寻找subset了
# 		如果 arr[i] > s: 需要4，结果9, 不选。
# 		如果 i = 0，target - value[i] = arr[0] ： 剩下一个数正好是需要的数值.
#
#
# DP:
# 待求值为matrix—row，状态index为column，matrix中值的转移用到arr-value.
# 	    0 1 2 3 4 5 6 7 8 9
# 3   0 F
# 34  1
# 4   2
# 12  3
# 5   4
# 2   5
#
#  @Author: Amber Hsia

import numpy as np

def rec_solution(arr, i, s):	 # s=剩余待加量

	if s == 0:
		return True
	elif arr[i] > s:
		return rec_solution(arr, i-1, s)
	elif i == 0:
		return s == arr[i]
	else:
		A = rec_solution(arr, i-1, s-arr[i])
		B = rec_solution(arr, i-1, s)
		return A or B


def dp_solution(arr, s):
	dp = np.zeros((len(arr), s+1), dtype=bool)

	dp[0, :] = False
	dp[:, 0] = False
	dp[0, arr[0]] = True

	for i in range(1, len(arr)):
		for j in range(1, s+1):
			if arr[i] > j: # 只考虑上边
				dp[i, j] = dp[i-1, j]
			else:
				A = dp[i-1, j-arr[i]]
				B = dp[i-1, j]
				dp[i, j] = A or B
	r, c = dp.shape

	return dp[r-1,c-1]



arr = [3,34,4,12,5,2]
print(dp_solution(arr, 9))