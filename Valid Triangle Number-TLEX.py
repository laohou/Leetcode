import itertools


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        iters = itertools.combinations(nums, 3)
        result = 0
        for it in iters:
            if self.isValidTriangle(it):
                result += 1
        return result

    def isValidTriangle(self, t):
        t = sorted(t)
        if t[0]+t[1] > t[2]:
            return True
        return False



if __name__ == '__main__':
    s = Solution()
    print s.triangleNumber([1,2,3,4,5,6])
    print s.triangleNumber([2,2,3,4])
    print s.triangleNumber([82,15,23,82,67,0,3,92,11])