class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = " " +text1
        text2 = " " +text2
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for j in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[n-1][m-1]

        # def solve(i,j,dp):
        #     if i<0 or j<0:
        #         return 0
        #     if (i,j) in dp: return dp[(i,j)]
        #     dp[(i,j)] =  1 + solve(i-1,j-1,dp) if text1[i]==text2[j] else max(solve(i-1,j,dp),solve(i,j-1,dp))
        #     return dp[(i,j)]
        # return solve(len(text1)-1,len(text2)-1,{})