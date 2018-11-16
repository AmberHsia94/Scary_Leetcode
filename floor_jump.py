# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # when choose = (1, 2), same as Fibonacci problem
        # now choose = (1, 2, n)
        # 递归的规律：f(n) = 2^(n-1)
        return 2 ** (number - 1)


