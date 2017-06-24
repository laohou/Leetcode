class Solution(object):
    def __init__(self):
        self.maxLen = 0
        self.low = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)

        if length == 0:
            return ''
        elif length == 1:
            return s

        i = 0
        while i < length:
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i+1)
            i += 1

        return s[self.low:self.low+self.maxLen]

    def extendPalindrome(self, s, left, right):
        length = len(s)
        while right < length and left >= 0 and s[left] == s[right]:
            right += 1
            left -= 1
        if right - left - 1 > self.maxLen:
            self.low = left + 1
            self.maxLen =right - left -1


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('babad')
    s = Solution()
    print s.longestPalindrome('cbbd')
    s = Solution()
    print 'bb pal:', s.longestPalindrome('bb')