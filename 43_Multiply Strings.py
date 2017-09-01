# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        length1 = len(num1)
        length2 = len(num2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        nums = [0 for _ in range(length1+length2)]

        for i in range(length1):
            for j in range(length2):
                nums[i+j] += (int(num1[i]) * int(num2[j]))

        carry = 0
        digits = []
        for d in nums:
            s = carry + d
            carry = s // 10
            digits.append(str(s % 10))

        result = digits[::-1]
        sub_index = 0
        for x in range(length1+length2-1):
            if result[x] == '0':
                sub_index += 1
            else:
                break


        return ''.join(result[sub_index:])

if __name__ == '__main__':
    num1 = '123'
    num2 = '234'
    print Solution().multiply(num1, num2)

    print Solution().multiply('9915', '9912')
    print Solution().multiply('9', '8')