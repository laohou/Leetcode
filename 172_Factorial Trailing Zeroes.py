# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given an integer n, return the number of trailing zeroes in n!.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        result = 0
        while n / i >= 1:
            result += n / i
            i *= 5
        return result

if __name__ == '__main__':
    assert Solution().trailingZeroes(5) == 1