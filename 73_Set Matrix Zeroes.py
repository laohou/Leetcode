# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])

        row_set = set()
        col_set = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(col):
                matrix[i][j] = 0

        for j in col_set:
            for i in range(row):
                matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [[1, 0, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 0],
              [1, 1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [1, 0, 0, 0]]

    m2 = [[0]]
    Solution().setZeroes(m2)
    print m2