# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset, max_len = set(nums), 0
        for n in set(nums):
            temp = n+1
            set_len = 1
            while temp in numset:
                set_len += 1
                numset.discard(temp)
                temp += 1

            temp = n - 1
            while temp in numset:
                set_len += 1
                numset.discard(temp)
                temp -= 1

            max_len = max(set_len, max_len)
        return max_len
if __name__ == '__main__':
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4