from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r1, c1 = startPos
        r2, c2 = homePos
        cost = 0
        
        # Move row-wise towards homePos
        if r1 < r2:
            for r in range(r1 + 1, r2 + 1):
                cost += rowCosts[r]
        else:
            for r in range(r1 - 1, r2 - 1, -1):
                cost += rowCosts[r]
        
        # Move column-wise towards homePos
        if c1 < c2:
            for c in range(c1 + 1, c2 + 1):
                cost += colCosts[c]
        else:
            for c in range(c1 - 1, c2 - 1, -1):
                cost += colCosts[c]
        
        return cost
