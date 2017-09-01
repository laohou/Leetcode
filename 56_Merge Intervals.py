# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(%d, %d)' % (self.start, self.end)

from collections import deque
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """


        if not intervals:
            return []
        elif len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:(x.end, x.start))
        result = deque()
        temp = intervals[-1]
        length = len(intervals)


        index = length - 2
        while index >= 0:
            if temp.start <= intervals[index].end:
                if temp.start > intervals[index].start:
                    temp.start = intervals[index].start
                if temp.end < intervals[index].end:
                    temp.end = intervals[index.end]
            else:
                result.appendleft(str(temp))
                temp = intervals[index]
            index -= 1

        result.appendleft(str(temp))

        return list(result)

if __name__ == '__main__':
    print Solution().merge([])
    print Solution().merge([Interval(1,3),Interval(2,6),Interval(6,7),Interval(8,10),Interval(15,18),Interval(17,20)])
    print Solution().merge([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)])