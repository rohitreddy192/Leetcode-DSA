class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def profit(i,transactionsLeft, buy):
            if transactionsLeft == 0: return 0
            if i==len(prices): return 0
            if (i,transactionsLeft,buy) in memo: return memo[(i,transactionsLeft,buy)]
            prof = 0
            if buy:
                prof = max(profit(i+1,transactionsLeft,buy), -prices[i]+profit(i+1,transactionsLeft,not buy))
            else:
                prof = max(profit(i+1,transactionsLeft,buy), prices[i]+profit(i+1,transactionsLeft-1, not buy))
                
            memo[(i,transactionsLeft,buy)] = prof
            return prof
        return profit(0,2,True)