# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given an array of integers that is already sorted in ascending order,

find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,

where index1 must be less than index2. Please note that your returned answers (both index1 and index2)

are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9

Output: index1=1, index2=2


"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        if n == 0:
            return []

        start, end = 0, n - 1
        while start < end:
            while start < end and numbers[start] + numbers[end] > target:
                end -= 1
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            start += 1
        return []

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 15], 9)