# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a triangle, find the minimum path sum from top to bottom.

Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,

where n is the total number of rows in the triangle.
"""
import sys


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        dp = [[0 for _ in range(i)] for i in range(1, col + 1)]

        dp[row - 1] = triangle[row - 1]

        for i in range(row - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


if __name__ == '__main__':
    print Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])