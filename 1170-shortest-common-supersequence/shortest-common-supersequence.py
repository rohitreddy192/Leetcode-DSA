class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1, str2 = " "+str1, " "+str2
        n, m = len(str1), len(str2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(1,n):
            for j in range(1,m):
                if str1[i]==str2[j]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        i, j = n-1, m-1
        ans = ""
        while i>0 and j>0:
            if str1[i]==str2[j]:
                ans += str1[i]
                i -= 1
                j -= 1
            elif dp[i-1][j]>dp[i][j-1]:
                ans += str1[i]
                i -= 1
            else:
                ans += str2[j]
                j -= 1
        while i>0:
            ans += str1[i]
            i -= 1
        while j>0:
            ans += str2[j]
            j -= 1
        
        return ans[::-1]
        # [  c  a  b
        # a [0, 1, 1], 
        # b [0, 1, 2], 
        # a [0, 1, 2], 
        # c [1, 1, 2]
        # ]

        