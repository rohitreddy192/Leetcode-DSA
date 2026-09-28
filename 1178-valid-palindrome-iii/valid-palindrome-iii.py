class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # def isPalindrome(left, right):
        #     if s[left]!= s[right]:
        #         return False
            
        #     while s[left]==s[right]:
        #         left += 1
        #         right -= 1
            
        #     return left>=right
        
        @lru_cache(None)
        def solve(rem, left, right):
            if left>=right:
                return True

            if rem<0:
                return False
            
            if s[left]!=s[right]:
                return solve(rem-1, left+1,right) or solve(rem-1, left, right-1) if rem>0 else False
            
            else:
                return solve(rem, left+1, right-1)
            

        return solve(k,0,len(s)-1)