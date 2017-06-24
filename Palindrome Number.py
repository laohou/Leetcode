class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        low = 0
        high = len(s) -1
        while low <= high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1

        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(123)
    print s.isPalindrome(1)
    print s.isPalindrome(11)
    print s.isPalindrome(121)