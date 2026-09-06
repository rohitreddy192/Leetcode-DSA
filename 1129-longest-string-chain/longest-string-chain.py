class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        n = len(words)
        words.sort(key=len)

        def compare(i,j):
            if len(words[i])-len(words[j]) != 1:
                return False
            a = words[i]
            b = words[j]

            cnt = 0
            i, j = len(a)-1, len(b)-1
            while i>=0 and j>=0:
                if a[i]==b[j]:
                    i-=1
                    j -= 1
                else:
                    if cnt == 1: return False
                    i -= 1
                    cnt = 1

            return True

        dp = [1]*(n)
        maxi = 0
        for i in range(n):
            for j in range(i):
                if compare(i,j) and dp[j]+1>dp[i]:
                    dp[i] = 1 + dp[j]
            
            maxi = max(dp[i],maxi)
        
        return maxi