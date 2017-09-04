# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a m x n grid filled with non-negative numbers,

find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):
    def minPathSumRecur(self, m, n, table, grid, row, col):

        if table[m][n] == -1:
            table[m][n] = grid[row - m - 1][col - n - 1] + min(self.minPathSumRecur(m - 1, n, table, grid, row, col),
                                                               self.minPathSumRecur(m, n - 1, table, grid, row, col))

        return table[m][n]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        table = [[-1 for _ in range(col)] for _ in range(row)]

        table[0][0] = grid[row - 1][col - 1]

        for i in range(1, col):
            table[0][i] = table[0][i - 1] + grid[row-1][col - i - 1]

        for i in range(1, row):
            table[i][0] = table[i - 1][0] + grid[row - i - 1][col-1]


        return self.minPathSumRecur(row - 1, col - 1, table, grid, row, col)


if __name__ == '__main__':
    print Solution().minPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])