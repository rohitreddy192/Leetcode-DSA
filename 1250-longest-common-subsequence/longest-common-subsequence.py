class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(i,j,dp):
            if i<0 or j<0:
                return 0
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] =  1 + solve(i-1,j-1,dp) if text1[i]==text2[j] else max(solve(i-1,j,dp),solve(i,j-1,dp))
            return dp[(i,j)]
        return solve(len(text1)-1,len(text2)-1,{})