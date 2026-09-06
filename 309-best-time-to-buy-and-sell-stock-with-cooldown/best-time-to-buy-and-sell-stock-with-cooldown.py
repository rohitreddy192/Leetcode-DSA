class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def solve(i, buy):
            if i>=n:
                return 0

            pick = not_pick = 0

            if buy:
                pick = max(-prices[i] + solve(i+1,not buy), solve(i+1, buy))
            else:
                not_pick = max(prices[i]+solve(i+2,not buy), solve(i+1,buy))
                        
            return max(pick, not_pick)
        
        return solve(0, True)