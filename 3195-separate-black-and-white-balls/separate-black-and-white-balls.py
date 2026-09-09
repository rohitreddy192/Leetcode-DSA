class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        ans = 0

        for x in s:
            if x == '1':
                ones += 1
            else:
                ans += ones

        
        return ans