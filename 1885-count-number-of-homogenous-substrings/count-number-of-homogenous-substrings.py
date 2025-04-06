class Solution:
    def countHomogenous(self, s: str) -> int:
        st = ""
        i,j = 0, 0
        MOD = 10**9 + 7
        ans = 0
        for j in range(len(s)):
            if not st:
                st = s[j]
            
            elif st != s[j]:
                st = s[j]
                i = j
            ans = (ans + (j-i+1)%MOD)%MOD
        
        return ans