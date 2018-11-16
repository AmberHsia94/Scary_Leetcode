# coding=utf-8
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[6,10],[15,18]]
#       [[1,5],[2,3],[6,10],[15,18]]
# 输出: [[1,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6], [6,10] 重叠, 将它们合并为
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):

    # sort first
    def bubble_sort(self, intervals):
        for i in range(len(intervals)):
            for j in range(i, len(intervals)):
                if intervals[i].start > intervals[j].start:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        return intervals

    # merge next
    def merge(self, intervals):
        rt = []

        if len(intervals)>0: # edge checker
            intervals = self.bubble_sort(intervals)
            rt.append([intervals[0].start, intervals[0].end])
            rt_l = 0

            while True:
                if (rt[rt_l][1] >= intervals[0].start) and (rt[rt_l][1] <= intervals[0].end):
                    rt[rt_l][1] = intervals[0].end
                    intervals.pop(0)
                    if len(intervals) == 0:
                        break
                elif (rt[rt_l][0] <= intervals[0].start) and (rt[rt_l][1] >= intervals[0].end):
                    intervals.pop(0)
                    if len(intervals) == 0:
                        break
                else:
                    rt.append([intervals[0].start, intervals[0].end])
                    rt_l = rt_l + 1
            return rt
        else:
            return []

solution = Solution()
print(solution.merge([Interval(1,3),
                    Interval(5,10),
                    Interval(2,6),
                    Interval(7,18),
                    Interval(19,23),
                    Interval(15,20),
                    Interval(16,30),
                    Interval(21,25),
                    Interval(35,40),
                    Interval(45,50),
                    Interval(46,52),
                    Interval(53,54)]))

print(solution.merge([]))
print(solution.merge([Interval(4,5),Interval(1,4),Interval(0,1),]))
print(solution.merge([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)]))
