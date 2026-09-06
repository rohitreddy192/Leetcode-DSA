class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # 1, 2, 3 stones
        n = len(stoneValue)

        @cache
        def solve(idx, isAlice):
            if idx>=n:
                return 0
            
            if isAlice:
                ans = float("-inf")
            else:
                ans = float("inf")
            taken = 0
            for i in range(3):
                if idx + i >= n:
                    break

                taken += stoneValue[idx+i]
                if isAlice:
                    ans = max(ans, taken + solve(idx+i+1, not isAlice))
                else:
                    ans = min(ans, -taken + solve(idx+i+1, not isAlice))
            
            return ans
        
        ans = solve(0,True)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        else:
            return "Tie"
                    
                