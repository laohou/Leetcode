# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""

from collections import deque
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex == 2:
            return [1, 2, 1]
        result = []
        for i in range(0, rowIndex):
            temp = [1]
            for j in range(0, len(result)-1):
                temp.append(result[j]+result[j+1])
            temp.append(1)
            result = temp
        return result
if __name__ == '__main__':
    print Solution().getRow(3)
    print Solution().getRow(4)
    print Solution().getRow(5)