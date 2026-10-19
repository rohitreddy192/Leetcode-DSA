class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        text1 = " "+text1
        text2 = " "+text2

        n = len(text1)
        m = len(text2)
        maxi = 0
        dp = [[0 for _ in range(m)]for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
                maxi = max(dp[i][j], maxi)

        return maxi