# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # fibonacci--- add previous two nums as current number
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233…

        ########  递归
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.Fibonacci(n-1) + self.Fibonacci(n-2)

        ## 迭代
        # num_1 = 0
        # num_2 = 1
        # for i in range(n):
        #     num_1 = num_1 + num_2
        #     num_2 = num_1 - num_2
        #
        # return num_1

        ## dynamic programming -- non-repeating
        d = {0: 0, 1: 1}
        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]


    # 矩形覆盖问题
    # n = 1 - 只有横放一个矩形一种解决办法
    # n = 2 - 有横放一个矩形，竖放两个矩形两种解决办法
    # n = 3 - n = 2的基础上加1个横向，n = 1的基础上加2个竖向
    # n = 4 - n = 3的基础上加1个横向，n = 2的基础上加2个竖向
    # ·
    # ·
    # ·
    # n = n - n = f(n - 1) + f(n - 2)
    #
    # 斐波那契数列变种。。。。。

    # 跳台阶问题 



sol = Solution()
print(sol.Fibonacci(11))