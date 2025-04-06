class Solution:
    def maxPower(self, s: str) -> int:
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
            ans = max(ans,(j-i+1))

        return ans