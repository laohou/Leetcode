# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        length = len(nums)
        nums = sorted(nums)
        result = [[]]
        temp_size = 0
        for i in range(length):
            start = temp_size if i > 0 and nums[i] == nums[i-1] else 0
            temp_size = len(result)

            for j in range(start, temp_size):
                result.append(result[j] + [nums[i]])

        return result

if __name__ == '__main__':
    print Solution().subsetsWithDup([1,2,2,1])
    print Solution().subsetsWithDup([1,1, 1, 2])
    print Solution().subsetsWithDup([4,4,1,4])
    print Solution().subsetsWithDup([5,1,5,5,5])