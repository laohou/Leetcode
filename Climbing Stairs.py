class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs2(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    def climbStairs(self, n):
        if n<3:
            return n
        s=[]
        s.append(0),s.append(1),s.append(2)
        i=3
        while i<n:
            tmp=s[i-1]+s[i-2]
            s.append(tmp)
            i=i+1
        return s[n-1]+s[n-2]

if __name__=="__main__":
    solution = Solution()
    print solution.climbStairs(1)
