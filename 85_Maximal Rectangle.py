# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a 2D binary matrix filled with 0's and 1's,

find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix[0])
        result = 0
        heights = [0 for _ in range(n)]
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            heights.append(0)
            stack = [-1]
            for i in range(n+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    result = max(result, h*w)
                stack.append(i)
            heights.pop()
        return result


if __name__ == '__main__':
    print Solution().maximalRectangle([['1', '1', '0', '1', '0', '1'],
                                        ['0', '1', '0', '0', '1', '1'],
                                        ['1', '1', '1', '1', '0', '1'],
                                        ['1', '1', '1', '1', '0', '1']])

    print Solution().maximalRectangle(["10100","10111","11111","10010"])