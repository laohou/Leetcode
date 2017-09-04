# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.

 The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution:
    def uniquePathsRecur(self, m, n, table):
        if table[m][n] == -1:
            table[m][n] = self.uniquePathsRecur(m - 1, n, table) + self.uniquePathsRecur(m, n - 1, table)
        return table[m][n]

    def uniquePaths(self, m, n):
        table = [[-1 for j in xrange(n)] for i in xrange(m)]
        table[0][0] = 1
        for i in range(0, m):
            table[i][0] = 1
        for j in range(0, n):
            table[0][j] = 1
        return self.uniquePathsRecur(m - 1, n - 1, table)