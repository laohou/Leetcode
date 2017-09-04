# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""


class Solution(object):
    def uniquePathsRecur(self, m, n, table, grid):

        if m < 0 or n < 0:
            return 0

        if grid[m][n] == 1:
            return 0

        if table[m][n] == -1:
            table[m][n] = self.uniquePathsRecur(m - 1, n, table, grid) + self.uniquePathsRecur(m, n - 1, table, grid)

        return table[m][n]


    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return -1

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        table = [[-1 for _ in range(col)] for _ in range(row)]
        for i in range(0, row):
            if obstacleGrid[i][0] == 0:
                table[i][0] = 1
            else:
                table[i][0] = 0
                break
        for j in range(0, col):
            if obstacleGrid[0][j] == 0:
                table[0][j] = 1
            else:
                table[0][j] = 0
                break

        return self.uniquePathsRecur(row-1, col-1, table, obstacleGrid)


if __name__ == '__main__':
    # print Solution().uniquePathsWithObstacles([
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ])
    print Solution().uniquePathsWithObstacles([
        [1, 0]
    ])