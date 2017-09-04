# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a string S and a string T,

find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import defaultdict
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_length = sys.maxint
        min_start = min_length
        length = len(s)
        end = start = 0
        char_need = defaultdict(int)
        count_need = len(t)
        for c in t:
            char_need[c] += 1

        while end < length:
            if char_need[s[end]] > 0:
                count_need -= 1
            char_need[s[end]] -= 1
            end += 1
            while count_need == 0:
                if min_length > end - start:
                    min_length = end - start
                    min_start = start

                char_need[s[start]] += 1
                if char_need[s[start]] > 0:
                    count_need += 1
                start += 1

        return '' if min_length == sys.maxint else s[min_start:min_start+min_length]

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print  Solution().minWindow(S, T)
    print  Solution().minWindow('ab', 'a')
    print  Solution().minWindow('abc', 'b')