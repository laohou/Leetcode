# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            res = chr((n-1) % 26 + ord('A')) + res
            n = (n-1) / 26

        return res


if __name__ == '__main__':
    print Solution().convertToTitle(26) == 'Z'
    print Solution().convertToTitle(27) == 'AA'
    print Solution().convertToTitle(28) == 'AB'
    print Solution().convertToTitle(52) == 'AZ'
    print Solution().convertToTitle(53) == 'BA'
