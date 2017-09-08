# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,

add spaces in s to construct a sentence where each word is a valid dictionary word.

You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given

s = "catsanddog",

dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):

The wordDict parameter had been changed to a list of strings (instead of a set of strings).

Please reload the code definition to get the latest changes.
"""

from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dic = defaultdict(list)

        def dfs(self, s):
            if not s:
                return [None]
            if s in self.dic:
                return dic[s]
            result = []
            for word in wordDict:
                length = len(word)
                if s[:length] == word:
                    for r in dfs(s[length:]):
                        if r:
                            result.append(word + ' ' + r)
                        else:
                            result.append(word)
                dic[s] = result
            return result
        return dfs(s)

if __name__ == '__main__':
    Solution()