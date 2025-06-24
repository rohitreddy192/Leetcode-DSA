class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def solve(idx, target):
            if target==0: return 0
            if target<0: return float("inf")
            if idx==0: return target//coins[idx] if target%coins[idx]==0 else float("inf")

            return min(1 + solve(idx,target-coins[idx]), solve(idx-1,target))
        
        tmp = solve(len(coins)-1, amount)
        return tmp if tmp<=amount else -1