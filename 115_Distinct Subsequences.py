# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original

string by deleting some (can be none) of the characters without

disturbing the relative positions of the remaining characters.

(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0

        m = len(s)
        n = len(t)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] if s[i-1] != t[j-1] else dp[i-1][j-1] + dp[i-1][j]
        return dp[m][n]

if __name__ == '__main__':
    print Solution().numDistinct('rabbbit', 'rabbit')