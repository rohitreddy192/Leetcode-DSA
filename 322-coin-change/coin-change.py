class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def solve(i,target):
            if target<0: return float("inf")
            if target==0: return 0
            if target-coins[i]==0: return 1

            if i<0: return float("inf")

            return min(1 + solve(i, target-coins[i]), solve(i-1,target))

        tmp = solve(len(coins)-1, amount)
        return tmp if tmp!=inf else -1
        