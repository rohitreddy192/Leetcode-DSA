class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        k = 0
        while left<=right:
            if k>2: return False
            if s[left]!=s[right]:
                k += 1
            left+= 1
            right -=1

        return k<=2        
            