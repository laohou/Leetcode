# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Implement pow(x, n).
"""


class Solution(object):
    def __init__(self):
        self.pow_table = {0:1}

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x

        if len(self.pow_table) == 1:
            self.pow_table[1] = x

        if n in self.pow_table:
            return self.pow_table[n]
        else:
            self.pow_table[n] = self.myPow(x, n//2) * self.myPow(x, n//2) if n % 2 == 0 else x * self.myPow(x, n//2) * self.myPow(x, n//2)

        return self.pow_table[n]

if __name__ == '__main__':
    print Solution().myPow(2.0, 15)