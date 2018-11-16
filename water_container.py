# coding=utf-8
# left和right分别指向两端的木板。
# left和right都向中央移动，每次移动left和Right中间高度较小的
#（因为反正都是移动一次，宽度肯定缩小1，这时候只能指望高度增加来增加容量，肯定是替换掉高度较小的，才有可能找到更大的容量。）
# 看新桶子的容量是不是大于Vol_max，直到left和right相交。
def water_container(n):
    front = 0
    tail = len(n) - 1

    volume = (tail - front) * min(n[front], n[tail])

    while front < tail:
        if n[front] < n[tail]: # compare whose height is lower
            tail = tail - 1
        else:
            front = front + 1

        cur_volume = (tail - front) * min(n[front], n[tail])

        if cur_volume > volume:
            volume = cur_volume

    return volume




