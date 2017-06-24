class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        start = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        maxFlowerNum = 0
        length = len(flowerbed)
        index = 0

        while index < length:
            if flowerbed[index] == 1 and index>start:
                maxFlowerNum += ((index-start)/2)
                if flowerbed[start] == 1:
                   maxFlowerNum -= 1
                start = index
            index += 1

        if start < length-1 and flowerbed[length-1] == 0:
            maxFlowerNum += (length - 1 - start) / 2
            if flowerbed[start]==0:
                maxFlowerNum += 1

        if n <= maxFlowerNum:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    assert s.canPlaceFlowers(flowerbed, n) == False, "wrong"
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    assert s.canPlaceFlowers(flowerbed, n) == True, "wrong"
    assert s.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1) == False, "wrong"
    assert s.canPlaceFlowers([0], 1) == True, "wrong"
    assert s.canPlaceFlowers([0,0], 1) == True, "wrong"
    assert s.canPlaceFlowers([1,0], 1) == False, "wrong"