class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def solve(idx, amt):
            if amt<0: return 0
            if amt==0: return 1
            if idx==0 and coins[0]!=0: return 1 if amt%coins[0] == 0 else 0

            pick = solve(idx,amt-coins[idx])
            not_pick = solve(idx-1, amt)

            return pick + not_pick

        return solve(len(coins)-1, amount)