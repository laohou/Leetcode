class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums = sorted(nums)
        self.recurPermute(nums, 0, len(nums))
        return self.result

    def recurPermute(self, nums, l, r):
        if l == r-1:
            self.result.append(nums)
        else:
            for i in xrange(l, r):
                if i != l and nums[i] == nums[l]:
                    continue

                nums[l], nums[i] = nums[i], nums[l]
                self.recurPermute(nums[:], l + 1, r)


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([1,1,2])
    print s.permuteUnique([2,2,1,1])
    print s.permuteUnique([1])
    print s.permuteUnique([1, 1])
    print s.permuteUnique([1,1,1,1,1])