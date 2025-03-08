class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def solve(i,t, buy):
            if i==len(prices) or not t:
                return 0
            
            profit = 0
            if not buy:
                profit = max(-prices[i] + solve(i+1,t,True), solve(i+1,t,buy))
            elif buy:
                profit += max(prices[i]+solve(i+1,False, buy), solve(i+1,t,buy))
            return profit
        return solve(0,True, False)