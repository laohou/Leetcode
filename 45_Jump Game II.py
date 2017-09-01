# -*- coding: utf-8 -*-
__author__ = 'yghou'

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.

(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) < 2:
            return 0

        length = len(nums)
        jump, longest, reach = 0, 0, nums[0]
        for i in range(1, length):
            if longest < i:
                jump += 1
                longest = reach
            reach = max(reach, nums[i] + i)

        return jump


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([1, 2]) == 1
    assert Solution().jump([3, 2, 1]) == 1
    assert Solution().jump([1,2,1,1,1]) == 3