class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2==1: return False

        n = len(nums)
        totSum = sum(nums)
        target = totSum//2
        # @lru_cache(None)
        # def solve(idx, target):
        #     if target==0: return True
        #     if idx<0: return False

        #     pick = False
        #     if target>=nums[idx]:
        #         pick = solve(idx-1, target-nums[idx])
            
        #     not_pick = solve(idx-1,target)

        #     dp[idx][target] pick or not_pick

        
        # return solve(n-1,totSum//2)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        for i in range(n):
            for j in range(target+1):
                pick = False
                if j>=nums[i]:
                    pick = dp[i-1][j-nums[i]]
                
                not_pick = dp[i-1][j]

                dp[i][j] = pick or not_pick
        
        return dp[n-1][target]

