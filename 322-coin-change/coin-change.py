class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(i, rem):
            if rem==0: return 0
            if rem<0: return float("inf")
            if i==0: return rem//coins[i] if rem%coins[i]==0 else float("inf")

            return min(1 + solve(i, rem-coins[i]), solve(i-1,rem))
        
        tmp = solve(len(coins)-1, amount)

        return tmp if tmp<=amount else -1