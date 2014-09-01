class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit2(self, prices):
        if prices == None or len(prices) < 2:
            return 0
        profit=prices[-1]-prices[-2]
        del(prices[-1])
        if profit < 0:
            return self.maxProfit(prices)
        else:
            return profit + self.maxProfit(prices)
    def maxProfit(self,prices):
        if prices == None or len(prices) < 2:
            return 0
        max=0
        for i in reversed(range(0,len(prices))):
            profit=prices[i]-prices[i-1]
            if profit > 0:
                max +=profit
            del(prices[i])
        return max

if __name__ =="__main__":
    prices=[1,2,3,4,5,3,6,5,6]
    solution = Solution()
    print solution.maxProfit(prices)
        
