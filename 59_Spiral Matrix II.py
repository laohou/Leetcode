# -*- coding: utf-8 -*-
__author__ = 'yghou'

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0 for _ in range(n)] for _ in range(n)]

        left, right, top, bottom = 0, n, 0, n

        counter = 0
        size = n * n
        while counter < size:

            if counter >= size:
                return m

            for i in xrange(left, right):
                m[top][i] = counter + 1
                counter += 1
            top += 1

            for j in xrange(top, bottom):
                m[j][right-1] = counter + 1
                counter += 1
            right -= 1

            for i in xrange(right-1, left-1, -1):
                m[bottom-1][i] = counter + 1
                counter += 1
            bottom -= 1

            for j in xrange(bottom-1, top-1, -1):
                m[j][left] = counter + 1
                counter += 1
            left += 1

        return m


if __name__ == '__main__':
    print Solution().generateMatrix(3)
    print Solution().generateMatrix(4)
    print Solution().generateMatrix(5)