class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        def solve(i,j):
            m, n = len(text1), len(text2)
            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            
            maxi = 0
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if text2[i-1]==text1[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                maxi = max(dp[i][j],maxi)
            return n+m - 2*maxi
        
        return solve(0,0)
                