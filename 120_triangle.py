# coding=utf-8

# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
# use only O(n) extra space, where n is the total number of rows in the triangle.


# recursive
def triangle(tri):
    print(tri)
    if len(tri) == 1:
        return tri[0]
    elif len(tri) == 2:
        return min(tri[0]) + min(tri[1])
    elif len(tri) > 2:  # previous total num + min_num of current layer
        return triangle(tri[:len(tri)-1]) + min(tri[len(tri)-1])

# dp
# 采用由下到上的思想（这样最后只需要取出dp[0][0]就是答案）
# dp[i][j] = min(dp[i-1][j-1] if j-1>=0, dp[i-1][j]) + triangle[i][j]

def dp_triangle(tri):
    if tri is None:
        return
    if len(tri) == 1:
        return

    dp = [[0 for i in range(len(tri))] for j in range(len(tri[-1]))]

    for i in range(len(tri)-1, -1, -1): # last row
        for j in range(len(tri[i])):
            if i == len(tri)-1:
                dp[i][j] = tri[i][j]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+tri[i][j]
    # print dp
    return dp[0][0]


if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # print(len(tri))
    print(triangle(tri))
    print dp_triangle(tri)