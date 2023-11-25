class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        7, 1, 5, 3, 6, 4 
        for todaysPrice in prices[1:]:
            maxProfit = max(maxProfit, todaysPrice - buy )
            buy = min(buy,todaysPrice)
        return maxProfit
