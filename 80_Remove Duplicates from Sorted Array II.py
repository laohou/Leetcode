# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,

with the first five elements of nums being 1, 1, 2, 2 and 3.

It doesn't matter what you leave beyond the new length.


"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.remainKDuplicates(nums, 2)

    def remainKDuplicates(self, nums, k):
        count = 0
        for i in range(len(nums)):
            if count < k or nums[count - k] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
    print Solution().removeDuplicates([1, 2, 2, 2, 3]) == 4
    print Solution().removeDuplicates([1, 1, 1, 1, 1, 1, 1, 2, 2, 2,2,2, 3]) == 5
    #print Solution().removeDuplicates([1, 2]) == 2