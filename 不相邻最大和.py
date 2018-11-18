# coding=utf-8

# 从数组中选出不相邻的数字，使其的和最大。
# [1， 2， 4， 1， 7， 8， 3]
#
# OPT = max(选， 不选)：
# 		选： v_i + OPT（i-2）
# 		不选： OPT（i-1）


def  solution(arr):
	# intialize the first condition
	opt = {}

	opt[0] = 1
	opt[1] = 2

	for i in range(2, len(arr)):
		opt[i] = max(opt[i-1], opt[i-2]+arr[i])
	return opt

print(solution([1,2,4,1,7,8,3]))




