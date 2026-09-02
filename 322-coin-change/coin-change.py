class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def solve(idx,rem):
            if rem==0: return 0
            if rem<0: return float("inf")
            if idx==0: return rem//coins[idx] if rem%coins[idx]==0 else float("inf")

            return min(solve(idx-1, rem), 1 + solve(idx,rem-coins[idx]))

        res = solve(len(coins)-1,amount)

        if res>amount:
            return -1

        return res