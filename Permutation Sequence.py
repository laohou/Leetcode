class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """


        nums = [i for i in range(1, n+1)]
        factorial = [1 for i in xrange(n+1)]
        result = []
        for i, num in enumerate(nums):
            factorial[i+1] *= factorial[i]*num

        k -= 1
        i = 1
        while i <= n:
            index = k/factorial[n-i]
            result.append(str(nums[index]))
            del nums[index]
            k -= index*factorial[n-i]
            i += 1
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(3, 3)=='213'
    print s.getPermutation(2, 2) == '21'
