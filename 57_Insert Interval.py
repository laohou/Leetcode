# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
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
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals and not newInterval:
            return []

        intervals.append(newInterval)
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
    print Solution().insert([], None)
    print Solution().insert([Interval(1,3),Interval(2,6),Interval(6,7),Interval(8,10),Interval(15,18),Interval(17,20)], Interval(1,10))
    print Solution().insert([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)], Interval(2,22))
