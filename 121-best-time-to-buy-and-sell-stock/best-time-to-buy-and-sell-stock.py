class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxSell = 0
        for idx, price in enumerate(prices):
            buy = min(buy, price)
            maxSell = max(price-buy, maxSell)
        
        return maxSell