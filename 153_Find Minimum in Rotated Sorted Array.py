# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
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
        # elif n == 1:
        #     return nums[0]
        # elif n == 2 or n == 3:
        #     return min(nums)

        low, high = 0, n-1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

if __name__ == '__main__':
    assert Solution().findMin([4, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2, 3]) == 0
    assert Solution().findMin([3, 1, 2]) == 1
    assert Solution().findMin([5, 1, 2, 3, 4]) == 1
    assert Solution().findMin([4, 5, 5, 1, 1, 2, 3]) == 1