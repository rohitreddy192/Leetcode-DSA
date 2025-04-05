class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = {}
        def solve(i):
            if i==n: return 0

            if i in dp: return dp[i]

            len = 0
            maxi = 0
            maxAns = 0
            for j in range(i, min(n,i+k)):
                len += 1
                maxi = max(maxi, arr[j])
                sum = maxi*len + solve(j+1)
                maxAns = max(sum, maxAns)
            
            dp[i] = maxAns
            return dp[i]
        
        return solve(0)