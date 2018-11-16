# coding=utf-8
# 找出数组numbers中的两个数，它们的和为给定的一个数target，并返回这两个数的索引，
# 注意这里的索引不是数组下标，而是数组下标加1。比如numbers={2,7,11,17}; target=9。那么返回一个元组(1,2)。
# 这道题不需要去重，对于每一个target输入，只有一组解，索引要按照大小顺序排列。
def two_sum(n, target):
    front = 0
    tail = len(n)-1

    #sort elements by quick-sort
    #O(nlogn)
    sorted_n = sorted(n)
    print(sorted_n)

    # use two pointers from start++ and from end-- respectively
    # O(n)
    while front < tail:
        # print(front, tail)
        if sorted_n[front] + sorted_n[tail] == target:
            # print(front, tail)
            break
        elif sorted_n[tail] > target - sorted_n[front]:
            tail = tail - 1
        elif sorted_n[tail] < target - sorted_n[front]:
            front = front + 1

    # find idx of previous unsorted n
    item1= sorted_n[front]
    item2= sorted_n[tail]

    return [n.index(item1), n.index(item2)]


# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: Elements in a triplet (a,b,c) must be in non-descending order.
# The solution set must not contain duplicate triplets.
def three_sum(n):
    front = 0
    tail = len(n)-1

    # sorted
    n_sorted = sorted(n)
    # print(n_sorted)
    result = []

    while front < len(n_sorted)-1 and n_sorted[front]<=0: # make n_sorted[front] is the smallest negative num in the array
        mid = front + 1
        # print(n_sorted[front], n_sorted[mid], n_sorted[tail])
        target = -n_sorted[front]
        while mid < tail:
            if n_sorted[mid] + n_sorted[tail] == target:
               result.append([n_sorted[front], n_sorted[mid], n_sorted[tail]])
               break
            elif n_sorted[mid] + n_sorted[tail] > target:
                tail = tail - 1
            elif n_sorted[mid] + n_sorted[tail] < target:
                mid = mid + 1
        front = front + 1

    return result



if __name__ == '__main__':
    n = [1, 3, 4, 5, 8, 11, 7, 6]
    target = 10
    print(two_sum(n, target))

    # S = [-1, 0, 1, 2, -1, -4]
    # print(three_sum(S))


