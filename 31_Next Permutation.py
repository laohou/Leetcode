# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return

        target_index = 0
        change_index = 0

        for i in xrange(length-1, 0, -1):
            if nums[i] > nums[i-1]:
                target_index = i-1
                break

        for i in xrange(length-1, -1, -1):
            if nums[i] > nums[target_index]:
                change_index = i
                break

        nums[target_index], nums[change_index] = nums[change_index], nums[target_index]

        if target_index == change_index == 0:
            nums.reverse()
        else:
            nums[target_index+1:] = reversed(nums[target_index+1:])


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]

    nums3 = [1, 1, 5]
    s.nextPermutation(nums1)
    print nums1


    s.nextPermutation(nums2)
    print nums2

    s.nextPermutation(nums3)
    print nums3
