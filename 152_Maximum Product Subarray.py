# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        elif n == 1:
            return nums[0]
        local_max = local_min = nums[0]
        result = nums[0]
        for i in range(1, n):
            local_max, local_min = max(nums[i], local_min*nums[i], local_max*nums[i]), min(nums[i], local_min*nums[i], local_max*nums[i])

            result = max(result, local_max)

        return result

if __name__ == '__main__':
    #assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-4,-3,-2]) == 12