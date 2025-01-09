class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(i,target):
            if target==0: return 0
            if target<0: return amount+1
            if i==0:
                return amount+1 if target%coins[0]!=0 else target//coins[0]
            return min(1 + solve(i,target-coins[i]),solve(i-1,target))

        tmp = solve(len(coins)-1,amount)
        return tmp if tmp<=amount else -1