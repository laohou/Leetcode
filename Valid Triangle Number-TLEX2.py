class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 0
        k = 0
        totalNum = 0
        length = len(nums)
        while i < length - 2:
            j = i+1
            while j < length -1:
                k = j+1
                while k < length:
                    if self.isValidTriangle((nums[i],nums[j], nums[k])):
                        totalNum += 1
                    k += 1
                j += 1
            i += 1
        return totalNum

    def isValidTriangle(self, t):
        if abs(t[0] + t[1]) > t[2] and abs(t[0]-t[1])<t[2]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print s.triangleNumber([1,2,3,4,5,6])
    print s.triangleNumber([2,2,3,4])
    print s.triangleNumber([43,88,91,17,28,21,7,26,100,81,54,55,85,28,80,75,29,98,52,68,74,29,18,5,99,40,27,67,46,91,52,35,60,97,11,32,51,60,90,68,65,95,65,66,36,62,59,77,44,8,62,99,22,53,36,10,56,29,48,15,22,49,69,48,72,39,50,34,41,43,76,96,82,31,31,40,13,86,97,8,23,69,30,25,31,29,35,82,28,91,19,47,81,48,31,31,89,86,68,86])