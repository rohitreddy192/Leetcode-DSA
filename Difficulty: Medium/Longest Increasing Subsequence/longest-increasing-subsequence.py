class Solution:
    def lis(self, arr):
        n = len(arr)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j] and dp[j]+1>dp[i]:
                    dp[i] = 1 + dp[j]
        
        return max(dp)