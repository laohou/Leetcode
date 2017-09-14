# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""

Compare two version numbers version1 and version2.

If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three",

it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        num1=version1.split('.')
        num2=version2.split('.')
        while len(num1) or len(num2):
            if len(num1)==0:
                num1=[0]
            elif len(num2)==0:
                num2=[0]
            else:
                i1=int(num1[0])
                i2=int(num2[0])
                if i1<i2:
                    return -1
                elif i1>i2:
                    return 1
                else:
                    num1=num1[1:]
                    num2=num2[1:]
        return 0


if __name__ == '__main__':
    assert Solution().compareVersion('0.1', '1.2') == -1
    assert Solution().compareVersion('1.1', '1.2') == -1
    assert Solution().compareVersion('01', '1') == 0