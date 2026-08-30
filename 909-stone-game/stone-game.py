class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        maximize_alice = 0
        total = sum(piles)

        @cache
        def solve(i,j, alice_turn):
            if i>j:
                return 0
            if alice_turn:
                return max(piles[i]+solve(i+1,j,not alice_turn), piles[j]+solve(i,j-1,not alice_turn))

            else:
                return min(piles[i]+solve(i+1,j,not alice_turn), piles[j]+solve(i,j-1, not alice_turn))

        
        maximize_alice = solve(0,len(piles)-1, True)
        return total-maximize_alice < total/2