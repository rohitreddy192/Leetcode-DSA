class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def solve(idx, buy, transactionsLeft):
            if idx==n:
                return 0
            
            if transactionsLeft == 0:
                return 0
                
            if not buy and transactionsLeft>0:
                return max(-prices[idx] + solve(idx+1, True, transactionsLeft), solve(idx+1, buy, transactionsLeft))

            else:
                return max(prices[idx]+solve(idx+1,False, transactionsLeft-1), solve(idx+1, buy, transactionsLeft))


        return solve(0,False,2)