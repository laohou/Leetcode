class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A==None:
            return 0
        length= len(A)
        time = A.count(elem)
        for i in range(0,time):
            A.remove(elem)
        return length - time

if __name__ == "__main__":
    solution = Solution()
    print solution.removeElement([],0)
    print solution.removeElement([4,5],4)
