class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        def isPalindrome(y):
            return y==y[::-1]

        @lru_cache(None)
        def solve(i):
            if i==n: return 0

            min_cost = 1e9
            for k in range(i,n):
                
                if isPalindrome(s[i:k+1]):
                    cost = 1 + solve(k+1)

                min_cost = min(cost,min_cost)
            
            return min_cost
        
        return solve(0)-1