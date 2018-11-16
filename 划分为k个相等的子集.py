# coding=utf-8

# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000


# 递归来做，1. 求出数组的所有数字之和sum，判断sum是否能整除k，不能整除的话直接返回false。
# 2. 需要一个visited数组来记录哪些数组已经被选中了，然后调用递归函数，
# 我们的目标是组k个子集合，是的每个子集合之和为target = sum/k。
# 我们还需要变量start，表示从数组的某个位置开始查找，curSum为当前子集合之和，
# 在递归函数中，如果k=1，说明此时只需要组一个子集合，那么当前的就是了，直接返回true。
# 如果curSum等于target了，那么我们再次调用递归，此时传入k-1，start和curSum都重置为0，因为我们当前又找到了一个和为target的子集合，要开始继续找下一个。
# 否则的话就从start开始遍历数组，如果当前数字已经访问过了则直接跳过，否则标记为已访问。
# 然后调用递归函数，k保持不变，因为还在累加当前的子集合，start传入i+1，curSum传入curSum+nums[i]，因为要累加当前的数字，如果递归函数返回true了，则直接返回true。
# 否则就将当前数字重置为未访问的状态继续遍历
def subspace(alist, k):
    if alist is None:
        return False
    if k == 1:
        return True
    if sum(alist)%k != 0:
        return False

    visited = []
    if k in alist:
        visited.append(k)
        alist.remove(k)
    else:





