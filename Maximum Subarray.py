import sys

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        length=len(A)
        maxSum=0
        result=0
        i=0
        if length==1:
            return A[0]
        if max(A)<0:
            return max(A)
        while i<length:
            if maxSum+A[i]>=0:
                maxSum += A[i]
                if result < maxSum:
                    result = maxSum
            else:
                maxSum=0
            i+=1
            
        return result

if __name__=="__main__":
    solution=Solution()
    print solution.maxSubArray([4,-1,2,1])           
