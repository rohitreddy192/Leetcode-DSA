class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def solve(i,j):
            if i<0 or j<0:
                return 0
            return 1 + solve(i-1,j-1) if text1[i]==text2[j] else max(solve(i-1,j),solve(i,j-1))
        return solve(len(text1)-1,len(text2)-1)