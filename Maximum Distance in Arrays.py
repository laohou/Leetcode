import Queue
import sys
class Solution(object):

    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result = -sys.maxint
        length = len(arrays)
        if length > 1:
            index = 2
            maxQueue= [1, 0] if arrays[0][-1] > arrays[1][-1] else [0, 1]
            minQueue = [1, 0] if arrays[0][0] < arrays[1][0] else [0, 1]
            while index < length:
                maxPos = maxQueue[1]
                minPos = minQueue[1]
                maxVal = arrays[maxPos][-1]
                minVal = arrays[minPos][0]
                secondaryMaxPos = maxQueue[0]
                secondaryMaxVal = arrays[secondaryMaxPos][-1]
                secondaryMinPos = minQueue[0]
                secondaryMinVal = arrays[secondaryMinPos][0]

                arrMin = arrays[index][0]
                arrMax = arrays[index][-1]
                if arrMin < minVal:
                    minQueue[0] =minQueue[1]
                    minQueue[1] = index
                elif arrMin < secondaryMinVal:
                    minQueue[0] = index

                if arrMax > maxVal:
                    maxQueue[0] = maxQueue[1]
                    maxQueue[1] = index
                elif arrMax > secondaryMaxVal:
                    maxQueue[0] = index

                index += 1
            for i in maxQueue:
                for j in minQueue:
                    if i != j:
                        if arrays[i][-1] - arrays[j][0] > result:
                            result = arrays[i][-1] - arrays[j][0]

        return result if result != -sys.maxint else 0

if __name__ == '__main__':
    s = Solution()
    print s.maxDistance([[1,2,3],[4,5],[1,2],[2,3]])==4
    print s.maxDistance([[-10,-9,-9,-3,-1,-1,0],[-5],[4],[-8],[-9,-6,-5,-4,-2,2,3],[-3,-3,-2,-1,0]])==14
    print s.maxDistance([[1,5], [3,4]])==3
    print s.maxDistance([[1,2,3],[4,5],[1,2,3]])==4
    print s.maxDistance([[-5,-2,0,1,1,2],[-7,-6,-3],[-8,-7,-4,-4,0,2,3,4]])==11