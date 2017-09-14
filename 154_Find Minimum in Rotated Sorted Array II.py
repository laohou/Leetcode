# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None

        low, high = 0, n-1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                low = mid + 1
        return nums[low]

if __name__ == '__main__':
    # assert Solution().findMin([3,3,1,3]) == 1
    # assert Solution().findMin([4, 6, 7, 0, 1, 2]) == 0
    # assert Solution().findMin([4, 5, 6, 7, 0, 1, 2, 3]) == 0
    # assert Solution().findMin([3, 1, 2]) == 1
    # assert Solution().findMin([5, 1, 2, 3, 4]) == 1
    # assert Solution().findMin([4, 5, 5, 1, 1, 2, 3]) == 1
    assert Solution().findMin([1,1,0,1,1,1,1,1,1,1,1,1]) == 0