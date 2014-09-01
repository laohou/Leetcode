class Solution:
    
    def singleNumber(self, A):
        result = A[0]
        for i in range(1, len(A)):
            result ^= A[i]

        return result

if __name__ == "__main__":
        solution = Solution()
        print solution.singleNumber([1,2,2,4,5,1,4])
