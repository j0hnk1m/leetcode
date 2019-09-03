class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            fluc = prices[i+1]-prices[i]
            if fluc > 0:
                profit += fluc
        return profit
