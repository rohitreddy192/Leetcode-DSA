class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def solve(i, buy, k):
            if k==0: return 0
            if i==n:
                return 0

            pick = not_pick = 0

            if buy:
                pick = max(-prices[i] + solve(i+1,not buy,k), solve(i+1, buy, k))
            else:
                not_pick = max(prices[i]+solve(i+1,not buy,k-1), solve(i+1,buy,k))
                        
            return max(pick, not_pick)
        
        return solve(0, True, 2)