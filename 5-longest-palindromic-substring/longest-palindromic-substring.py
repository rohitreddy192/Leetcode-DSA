class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s == s[::-1]
        ans = ""
        maxi = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if isPalindrome(s[i:j]) and maxi<(j-i+1):
                    maxi = j-i+1
                    ans = s[i:j]
        return ans