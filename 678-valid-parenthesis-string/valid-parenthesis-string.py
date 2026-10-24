class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def solve(idx, val):
            if val<0: return False
            
            if idx==n:
                return val==0
            
            st = s[idx]

            if st in "()":
                return solve(idx+1, val + (1 if st == "(" else -1))
            
            else:

                return solve(idx+1, val+1) or solve(idx+1,val-1) or solve(idx+1, val)

        return solve(0,0)