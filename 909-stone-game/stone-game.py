class Solution:
    def stoneGame(self, piles: List[int]) -> bool:


        @cache
        def solve(l,r):
            if l>=r:
                return 0
            pick_from_left = max(piles[l] + solve(l+1,r-1)-piles[r] ,piles[l] + solve(l+2,r)-piles[l+1])
            pick_from_right = max(piles[r] + solve(l,r-2)-piles[r-1], piles[r]+ solve(l+1,r-1)-piles[l])

            return max(pick_from_left, pick_from_right)
        
        return solve(0,len(piles)-1) > 0
