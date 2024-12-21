class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def solve(i,amount):
            if amount == 0: return 1
            if i<0 or amount<0: return 0
            if i==0: return 1 if amount%coins[0]==0 else 0

            return solve(i-1,amount) + solve(i,amount-coins[i])
        
        return solve(len(coins)-1, amount)