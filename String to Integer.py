import sys
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        #this is keng
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        length = len(s)
        if length==0:
            return 0
        s = s.strip()
        result = 0

        index = 0
        for i in s:
            if result < MAX_INT and i.isdigit():
                result = 10*result + int(i)
            elif index>0:
                break
            index += 1

        if s[0] == '-':
            result = -result
        elif s[0]!='+' and not s[0].isdigit():
            return 0

        if result > MAX_INT:
            result = MAX_INT
        elif result < MIN_INT:
            result = MIN_INT


        return result

if __name__ == '__main__':
    s = Solution()
    print "max int:"+ str(sys.maxint)
    print s.myAtoi('+12')
    print s.myAtoi('-12')
    print s.myAtoi('12')
    print s.myAtoi('+-12')
    print s.myAtoi("  -0012a42")
    print s.myAtoi("2147483648")

