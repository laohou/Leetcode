class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.recurPermute(nums, 0, len(nums)-1)
        return self.result
    def recurPermute(self, nums, l, r):
        if l == r:
            self.result.append(nums[:])
        else:
            for i in xrange(l, r+1):
                nums[l], nums[i] = nums[i], nums[l]
                self.recurPermute(nums, l+1, r)
                nums[l], nums[i] = nums[i], nums[l]

if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3])