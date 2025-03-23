class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s==s[::-1]
        le = 0
        for i in range(1, len(s)):
            if isPalindrome(s[:i+1]):
                le = i
        
        return s[le+1:][::-1] + s