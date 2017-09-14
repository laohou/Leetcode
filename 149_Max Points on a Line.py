# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


import sys
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        result = 0
        slope_map = {}
        for i in range(length):
            slope_map.clear()
            same = 0
            for j in range(i+1, length):
                slop = 0.0
                dx, dy = points[i].x - points[j].x, points[i].y-points[j].y
                if dx == dy == 0:
                    same += 1
                    continue
                if dx == 0:
                    slope = sys.float_info.max
                else:
                    slope = float(dy) / float(dx)

                if slope in slope_map:
                    slope_map[slope] += 1
                else:
                    slope_map[slope] = 2
            result = max(result, same + 1)
            for val in slope_map.values():
                result = max(result, val + same)
        return result

if __name__ == '__main__':
    p1 = Point(0,0)
    #[[0,0],[94911151,94911150],[94911152,94911151]]
    p2 = Point(94911151, 94911150)
    p3 = Point(94911152, 94911151)

    assert Solution().maxPoints([p1, p2, p3]) == 2