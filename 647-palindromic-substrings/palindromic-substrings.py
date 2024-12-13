class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            return s[::-1] == s

        cnt = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if isPalindrome(s[i:j]):
                    cnt += 1
        return cnt