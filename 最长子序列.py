# coding=utf-8

# 最长公共子序列， 不要求连续
# 序列a共有m个元素，序列b共有n个元素，分别当作矩阵的行与列, move方向：斜下， 右， 下
# 如果a[m-1]==b[n-1]，那么最长公共子序列长度就是a[:m-1]和b[:n-1]的最长公共子序列长度+1；
# 如果a[m-1]!=b[n-1]，那么最长公共子序列长度就是max（a[:m-1]和b[:n]的最长公共子序列长度，a[:m]和b[:n-1]的最长公共子序列长度）

# a = 'abcdefgh'
# b = 'hcefgk'

import numpy as np

def max_substring(a, b):
    m = len(a)+1
    n = len(b)+1

    max_len = np.zeros((m,n)) #[[0 for j in range(n)] for i in range(m)]
    flag = np.zeros((m,n)) #[[0 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if a[i - 1] == b[j - 1]:
                max_len[i][j] = max_len[i - 1][j - 1] + 1
                flag[i][j] = 0  # mark flag to track where it comes from: 斜上方向
            else:
                if max_len[i - 1][j] > max_len[i][j - 1]:
                    max_len[i][j] = max_len[i - 1][j]
                    flag[i][j] = 1
                else:
                    max_len[i][j] = max_len[i][j - 1]
                    flag[i][j] = 2

    return max_len, flag


def print_LCS(max_len, flag, i, j):
    if i == 0 and j == 0:
        return

    # back-tracing
    if flag[i][j] == 0:
        print_LCS(max_len, flag, i - 1, j - 1)
        print max_len[i - 1]  # 这里同理，要输出x[i-1]
    elif flag[i][j] == 1:
        print_LCS(max_len, flag, i - 1, j)
    else:
        print_LCS(max_len, flag, i, j - 1)


str1 = 'abcdfsgdfg'
str2 = 'adwefevevgf'
max_len, flag = max_substring(str1, str2)
print flag
print_LCS(str1, flag, len(str1), len(str2))
