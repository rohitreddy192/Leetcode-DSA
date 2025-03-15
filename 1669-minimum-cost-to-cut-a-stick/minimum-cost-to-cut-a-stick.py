class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        @lru_cache(None)
        def solve(i,j):
            if i>j: return 0

            min_cost = 1e9
            for k in range(i,j+1):
                cost = (cuts[j+1] - cuts[i-1]) + solve(i,k-1)+solve(k+1,j)
                min_cost = min(min_cost,cost)
            
            return min_cost
        
        return solve(1,len(cuts)-2)