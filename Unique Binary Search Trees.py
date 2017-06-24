class Solution:
    # @return an integer
    def numTrees(self, n):
        if n < 0:
            return 0
        queryArr=[0,1,2,5]
        for i in range(4,n+1):
            m = 0
            j = i
            k = 1

            m+=queryArr[j-1]*2
            j -= 2
            while j>0:
                m+=queryArr[j]*queryArr[k]
                j-=1
                k+=1
            queryArr.append(m)
            
        return queryArr[n]

if __name__=="__main__":
    solution = Solution()
    print solution.numTrees(5)
