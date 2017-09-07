# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        result = []
        for i in range(len(s)):
            if self._is_palindrome(s[:i+1]):
                for r in self.partition(s[i+1:]):
                    result.append([s[:i+1]] + r)
        return result

    def _is_palindrome(self, s):
        end, start = len(s)-1, 0
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True



if __name__ == '__main__':
    Solution()