# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,

determine if s can be segmented into a space-separated sequence of one or more dictionary words.

You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).

Please reload the code definition to get the latest changes.
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        wordDict = set(wordDict)
        dp = [False for _ in range(length+1)]
        dp[0] = True
        for i in range(1, length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    s = "leetcode"
    dict = ["leet", "code"]
    print Solution().wordBreak(s, dict)