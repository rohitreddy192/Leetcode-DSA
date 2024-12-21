class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # @lru_cache(None)
        # def solve(i,t):
        #     if i<0 or t<0: return float("inf")
        #     if i==0: return t//coins[i] if(t%coins[i]==0) else float("inf")
        #     if t==0: return 0
        #     return min(1 + solve(i,t-coins[i]), solve(i-1,t))
        
        # tmp = solve(len(coins)-1,amount)
        # if amount == 0: return 0
        # return tmp if tmp!=float("inf") else -1

        n = len(coins)
        dp = [[1e9 for _ in range(amount+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        
        for i in range(1,amount+1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]
        
        for i in range(1,n):
            for j in range(1,amount+1):
                dp[i][j] = min(dp[i-1][j], (1+ dp[i][j-coins[i]] if j-coins[i]>=0 else 1e9))
        tmp = dp[n-1][amount]
        if tmp == 1e9: return -1
        return tmp