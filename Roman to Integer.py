class Solution:
    # @return an integer
    def romanToInt(self, s):
        if s==None:
            return 0
        length = len(s.upper())
        result = 0
        i=0
        while i < length:
            if s[i]=='M':
                result+=1000
            elif s[i]=='D':
                result+=500
            elif s[i]=='C':
                if i+1<length and s[i+1]=='M':
                    result += 900
                    i=i+1
                elif i+1<length and s[i+1]=='D':
                    result+=400
                    i=i+1
                else:
                    result+=100
            elif s[i]=='L':
                result+=50
            elif s[i]=='X':
                if i+1<length and s[i+1]=='C':
                    result+=90
                    i=i+1
                elif i+1<length and s[i+1]=='L':
                    result+=40
                    i=i+1
                else:
                    result+=10
            elif s[i]=='V':
                result+=5
            elif s[i]=='I':
                if i+1<length and s[i+1]=='V' :
                    result+=4
                    i=i+1
                elif i+1<length and s[i+1]=='X':
                    result+=9
                    i=i+1
                else:
                    result+=1
            i=i+1
        return result
                


if __name__=="__main__":
    solution = Solution()
    print solution.romanToInt("MMMCMXCIX")
