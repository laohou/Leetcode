# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        p_index, s_index, prev_p_index, prev_s_index = 0, 0, -1, -1

        s_length = len(s)
        p_length = len(p)

        while s_index < s_length:
            if p_index < p_length and (p[p_index] == s[s_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            elif p_index < p_length and p[p_index] == '*':
                p_index += 1
                prev_p_index = p_index
                prev_s_index = s_index
            elif prev_p_index != -1:
                prev_s_index += 1
                s_index = prev_s_index
                p_index = prev_p_index
            else:
                return False

        while p_index < p_length:
            if p[p_index] == "*":
                p_index += 1
            else:
                break

        return p_index == p_length


if __name__ == '__main__':
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", "?*") == True
    assert Solution().isMatch("aab", "c*a*b") == False
