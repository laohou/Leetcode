class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows <=1 or length <= 1:
            return s

        result = ''
        i = 0
        while i<length and i<numRows:
            idx = i
            result += s[idx]
            k = 1
            while idx < length:
                if i==0 or i== numRows-1:
                    idx += 2*numRows-2
                else:
                    if k&0x01:
                        idx += 2*(numRows-i-1)
                    else:
                        idx += 2*i
                if idx < length:
                    result += s[idx]
                k += 1
            i += 1
        return result
if __name__ == '__main__':
    s = Solution()
    print s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
