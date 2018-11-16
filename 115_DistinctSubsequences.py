# coding=utf-8
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
# Return 3.
#
# 题意解读：只可以用删除字符的方法从第一个字符串S变换到第二个字符串T，求出一共有多少种变换方法。


def num_of_edit(s, t):
    dp = [[0 for col in range(len(t))] for row in range(len(s))]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[0][0] == t[0][0]:
                dp[0][0] = 1

            if i != 0 and j !=0:
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]  # 正上方和斜上方
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

s="rabbbit"
t="rabbit"
print num_of_edit(s, t)