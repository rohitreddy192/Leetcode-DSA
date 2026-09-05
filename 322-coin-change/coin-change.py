class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(idx, amount):
            if amount == 0: return 0
            if amount < 0: return 1e9
            if idx==0: return amount//coins[idx] if amount%coins[idx]==0 else 1e9

            return min(1 + solve(idx, amount-coins[idx]), solve(idx-1, amount))
        
        ans = solve(len(coins)-1, amount)
        if ans > amount: return -1
        return ans