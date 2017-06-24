import itertools


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalNum = 0
        nums = sorted(nums)
        length = len(nums)
        for i in range(0, length-2):
            for j in range(i+1, length-1):
                k = self.binarySearch(nums, nums[i]+nums[j], j+1)
                totalNum = totalNum + k - j

        return totalNum

    def binarySearch(self, nums, num, start):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        return left-1

    def isValidTriangle(self, t):
        t = sorted(t)
        if t[0]+t[1] > t[2]:
            return True
        return False



if __name__ == '__main__':
    s = Solution()
    assert s.triangleNumber([1,2,3,4,5,6]) ==7, "wrong"
    assert s.triangleNumber([2,2,3,4])== 3, "wrong"
    assert s.triangleNumber([1,1,3,4]) == 0, "wrong"
    assert s.triangleNumber([82,15,23,82,67,0,3,92,11])==17, "wrong"