class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)

        @cache
        def solve(i,j):
            if i<0 : return j+1
            if j<0 : return i+1
            
            if word1[i]==word2[j]: return solve(i-1,j-1)
            else:
                insert = 1 + solve(i,j-1)
                delete = 1 + solve(i-1,j)
                replace = 1 + solve(i-1,j-1)

                return min(insert, delete, replace)
        
        return solve(n-1,m-1)