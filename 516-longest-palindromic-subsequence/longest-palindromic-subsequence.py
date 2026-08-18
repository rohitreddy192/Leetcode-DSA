class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:
        text2 = text1[::-1]
        n = len(text1)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        maxi = 0
        for i in range(1,n+1):

            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                maxi = max(maxi,dp[i][j])
        return maxi