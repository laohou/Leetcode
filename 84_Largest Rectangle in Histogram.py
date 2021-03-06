# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,

find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        result = 0
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h*w)
            stack.append(i)

        return result


if __name__ == '__main__':
    print Solution().largestRectangleArea([2,1,5,6,2,3])
    print Solution().largestRectangleArea([1,3,1,1,1,1])