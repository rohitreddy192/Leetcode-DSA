class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def solve(i,t):
            if i<0 or t<0: return float("inf")
            if i==0: return t//coins[i] if(t%coins[i]==0) else float("inf")
            if t==0: return 0
            return min(1 + solve(i,t-coins[i]), solve(i-1,t))
        
        tmp = solve(len(coins)-1,amount)
        if amount == 0: return 0
        return tmp if tmp!=float("inf") else -1