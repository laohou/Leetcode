class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A==None:
            return 0
        low = 0
        high = len(A)-1
        mid = 0
        while low <= high:
            mid = (high + low)/2
            if target < A[mid]:
                high = mid-1
            elif target > A[mid]:
                low = mid+1
            elif target == A[mid]:
                return mid
        
        if target > A[high]:
            return high+1
        elif target < A[low]:
            return low
        
if __name__=="__main__":
    solution = Solution()
    A=[4]
    print solution.searchInsert(A,4)
