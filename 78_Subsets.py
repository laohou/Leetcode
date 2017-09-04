# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for num in sorted(nums):
            result += [item + [num] for item in result]

        return result

if __name__ == '__main__':
    print Solution().subsets([1, 2, 3])