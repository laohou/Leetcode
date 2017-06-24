class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans=0
        neg=0
        for i in range(0,32):
            tmp=0
            neg=0
            bitOp=1<<i
            for j in A:
                tmpNum=j if j>0 else -j                    
                if tmpNum&bitOp:
                    tmp+=1
            if tmp%3!=0:
                ans|=bitOp
        for k in A:
            if k<0:
                neg+=1

        if neg%3:
            ans=-ans

        return ans

if __name__=="__main__":
    solution=Solution()
    print solution.singleNumber([-1])
    print -1&pow(2,31)
    print 1
