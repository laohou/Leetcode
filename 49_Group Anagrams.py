# -*- coding: utf-8 -*-
__author__ = 'yghou'

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams_map:
                anagrams_map[sorted_s].append(s)
            else:
                anagrams_map[sorted_s] = [s]

        result = []
        for v in anagrams_map.values():
            result.append(v)

        return result


if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])