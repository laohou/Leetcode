# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given two integers representing the numerator and denominator of a fraction,

 return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if numerator * denominator < 0:
            res += '-'
        num = abs(numerator)
        den = abs(denominator)
        res += str(num//den)
        num %= den
        if num == 0:
            return res

        res += '.'

        repeating_map = {}
        while num != 0:

            if num in repeating_map:
                index = repeating_map[num]
                res = res[:index] + '(' + res[index:] + ')'
                break
            else:
                repeating_map[num] = len(res)
            num *= 10
            res += str(num/den)
            num %= den

        return res


if __name__ == '__main__':
    print Solution().fractionToDecimal(2, 1)
    print Solution().fractionToDecimal(-1, 2)
    print Solution().fractionToDecimal(-1, 3)
    print Solution().fractionToDecimal(2, 3)
    assert Solution().fractionToDecimal(1, 6) == "0.1(6)"