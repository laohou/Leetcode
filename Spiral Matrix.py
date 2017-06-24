class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result=[]
        if len(matrix)==0:
            return result
        xMin=0
        yMin=0
        xMax=len(matrix[0])
        yMax=len(matrix)
        x=0
        y=0
        while True:
            y=yMin
            x=xMin
            while x<xMax:
                result.append(matrix[y][x])
                x+=1
            yMin += 1
            if yMin >= yMax:
                break
            
            x=xMax-1
            y=yMin
            while y<yMax:
                result.append(matrix[y][x])
                y += 1
            xMax -= 1
            if xMin >= xMax:
                break
            
            y=yMax-1
            x=xMax-1
            while x>=xMin:
                result.append(matrix[y][x])
                x -= 1
            yMax -= 1
            if yMin >= yMax:
                break

            x=xMin
            y=yMax-1
            while y>=yMin:
                result.append(matrix[y][x])
                y -= 1
            xMin += 1
            if xMin >= xMax:
                break
        return result
if __name__=="__main__":
    solution = Solution()
    print solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]] )
    print solution.spiralOrder([[]])
            
