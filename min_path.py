# coding=utf-8
import numpy as np
# Given a mxn grid, a robot is at top left corner, it can only move either down or right at any point
# find how many paths in total it can reach to the bottom right corner
# 正向思维，走一步保存一步
def total_paths(m, n):
    path = np.arange(m*n).reshape(m, n) # initialise 2d array

    for idx_row in range(m):
        for idx_col in range(n):
            if idx_row == 0 and idx_col == 0:
                path[0][0] = 1
            elif idx_row == 0:  # start corner line
                path[idx_row][idx_col] = path[idx_row][idx_col-1]
            elif idx_col == 0:  # start corner line
                path[idx_row][idx_col] = path[idx_row-1][idx_col]
            else:
                path[idx_row][idx_col] = path[idx_row-1][idx_col] + path[idx_row][idx_col-1]

    return path[m-1][n-1]


# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
#  which minimizes the sum of all numbers along its path.
#  Note: You can only move either down or right at any point in time.
def min_path(m, n):
    value_sum = np.zeros((m,n))  # initialise 2d array
    cur = np.arange(m * n).reshape(m, n)

    for row in range(m):
        for col in range(n):
            if row == 0:
                value_sum[row][col] = value_sum[row][col-1] + cur[row][col]
            elif col == 0:
                value_sum[row][col] = value_sum[row-1][col] + cur[row][col]
            else:
                value_sum[row][col] = max(value_sum[row-1][col], value_sum[row][col-1]) + cur[row][col]

    return value_sum[m-1][n-1]



# fellow up for total_paths
# consider randomly add some obstacles during the path, how many paths from top left to bottom right?
# obstacle is marked as 1 and empty space is 0
# 其实只需要把这些障碍位置的路径矩阵赋值为0即可：
def unique_path(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    path = np.arange(row_len * col_len).reshape(row_len, col_len)

    for idx_row in range(row_len):
        for idx_col in range(col_len):
            if matrix[idx_row][idx_col] == 1:
                path[idx_row][idx_col] = 0
            else:
                if idx_row == 0 and idx_col == 0:
                    path[0][0] = 1
                elif idx_row == 0:
                    path[idx_row][idx_col] = path[idx_row][idx_col - 1]
                elif idx_col == 0:
                    path[idx_row][idx_col] = path[idx_row - 1][idx_col]
                else:
                    path[idx_row][idx_col] = path[idx_row - 1][idx_col] + path[idx_row][idx_col - 1]

    return path[row_len - 1][col_len - 1]


# climbing stairs, which takes n stairs to reach the top
# each time you can choose take 1 step or 2 steps, how many distinct ways to reach the top
# n is a positive integer
def climb_stair(n):
    arr = np.zeros(n+1)

    for i in range(n+1):
        if i == 0:
            arr[i] = 1
        elif i == 1:
            arr[i] = 1
        else:
            arr[i] = arr[i-1] + arr[i-2]

    return arr[n]


# give an array of int, return the sum from position i to j
def target_sum(arr, i, j):
    arr_sum = np.zeros(j+1)

    for idx in range(i, j+1):
        if idx == i:
            arr_sum[idx] = arr[i]
        else:
            arr_sum[idx] = arr_sum[idx-1] + arr[idx]

    return arr_sum




# print(total_paths(3,3))
# print(min_path(3,3))
# print(unique_path([[2, 1, 5], [3, 2, 4], [5, 6, 7]]))
# print(climb_stair(4))
print(target_sum([1,2,3,4,5,6], 2, 4))
