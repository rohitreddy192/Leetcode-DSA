class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @lru_cache(None)
        # def solve(i,amount):
        #     if amount == 0: return 1
        #     if i<0 or amount<0: return 0
        #     if i==0: return 1 if amount%coins[0]==0 else 0

        #     return solve(i-1,amount) + solve(i,amount-coins[i])
        
        # return solve(len(coins)-1, amount)

        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i] = 1
        
        for i in range(1,n):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i]] if j-coins[i]>=0 else 0)
        
        return dp[n-1][amount]