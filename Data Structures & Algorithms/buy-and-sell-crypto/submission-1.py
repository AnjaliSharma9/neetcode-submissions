class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 100
        high = 0
        for i in prices:
            if i > i+1:
                low = min(low,prices[i+1])
            else:
                high = max(high,prices[i])
        profit = high - low 
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r += 1
        return maxP






       