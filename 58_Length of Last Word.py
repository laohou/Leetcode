# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',

return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        i = length - 1
        result = 0
        while i >= 0:
            if s[i] != ' ':
                while i >= 0 and s[i] != ' ':
                    result += 1
                    i -= 1
                return result
            i -= 1
        return 0



if __name__ == '__main__':
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("a") == 1
    assert Solution().lengthOfLastWord("a ") == 1
    assert Solution().lengthOfLastWord("abc ") == 3