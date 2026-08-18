class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        
        @cache
        def solve(idx, steps):
            if idx<0 or idx>=arrLen: return 0
            if steps<0: return 0
            if steps == 0:
                return 1 if idx==0 else 0

            # if idx==0 and steps>0:
            #     return (solve(idx+1, steps-1)%MOD + solve(idx, steps-1)%MOD)%MOD

            # if idx==arrLen-1 and steps>0:
            #     return (solve(idx-1, steps-1)%MOD + solve(idx, steps-1)%MOD)%MOD
            
            return (solve(idx+1, steps-1)%MOD + (solve(idx-1,steps-1)%MOD + solve(idx,steps-1)%MOD)%MOD)%MOD
            
        return solve(0,steps)