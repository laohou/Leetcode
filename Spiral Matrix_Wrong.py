
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
   
    #handle the matrix according different direction
    def specialDirection(self, matrix, direction,depth):
        arr = []
        rowLen = len(matrix[0])
        columnLen = len(matrix)
        if(direction == self.RIGHT):
            for i in range(depth, rowLen):
                arr.append(matrix[depth][i])
        elif(direction == self.LEFT):
            for i in reversed(range(depth, rowLen)):
                arr.append(matrix[columnLen-1-depth][i-1])
        elif(direction == self.DOWN):
            for i in range(depth,columnLen-1):
                arr.append(matrix[i+1][rowLen-1-depth])
        elif(direction == self.UP):
            for i in reversed(range(depth+1,columnLen)):
                arr.append(matrix[i-1][depth])
        print arr
        return arr

    def spiralOrder(self, matrix):
        result =[]
        rowLen = len(matrix[0])
        columnLen = len(matrix)
        visitedColumns = 0
        visitedRows = 0
        if(rowLen==0 or columnLen==0):
            return result
        min = rowLen if rowLen <= columnLen else columnLen
        depth = (min+1)/2

        for i in range(0,depth):
            if rowLen-visitedRows > 0:
               self.specialDirection(matrix,self.RIGHT,i)
               visitedRows = visitedRows+1
            if columnLen-visitedColumns >0:
                self.specialDirection(matrix,self.DOWN,i)
                visitedColumns += 1
            if rowLen-visitedRows > 0:
                self.specialDirection(matrix,self.LEFT,i)
                visitedRows+=1
            if columnLen-visitedColumns >0:
                self.specialDirection(matrix,self.UP,i)
                visitedColumns+=1
         
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
