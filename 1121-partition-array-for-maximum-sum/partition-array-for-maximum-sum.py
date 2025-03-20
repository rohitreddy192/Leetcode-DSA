class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @lru_cache(None)
        def solve(i):
            if i==n: return 0

            len = 0
            maxi = 0
            maxAns = 0
            for j in range(i, min(n,i+k)):
                len += 1
                maxi = max(maxi, arr[j])
                sum = maxi*len + solve(j+1)
                maxAns = max(sum, maxAns)
            
            return maxAns
        
        return solve(0)