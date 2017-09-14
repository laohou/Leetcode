# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1,

and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLIS= ans = 0
        size = len(nums)
        dp = [1] * size
        dz = [1] * size
        for x in range(size):
            for y in range(0, x):
                if nums[x] > nums[y]:
                    if dp[y] + 1 > dp[x]:
                        dp[x] = dp[y] + 1
                        dz[x] = dz[y]
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        maxLIS = max(dp + [0])
        ans = 0
        for p, z in zip(dp, dz):
            if p == maxLIS:
                ans += z
        return ans

if __name__ == '__main__':
    assert Solution().findNumberOfLIS([1,3,5,4,7]) == 2
    assert Solution().findNumberOfLIS([1,3,2,4,7]) == 2
    assert Solution().findNumberOfLIS([2, 2, 2, 2]) == 4
    assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3