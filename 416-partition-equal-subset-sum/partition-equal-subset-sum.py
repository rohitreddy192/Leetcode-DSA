class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(i,target):
            if i==0: return target==nums[i]
            if target==0: return True
            if i<0: return False
            return solve(i-1,target) or solve(i-1,target-nums[i])

        
        totalSum = sum(nums)
        if totalSum %2 == 1: return False
        n = len(nums)
        target = totalSum//2
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        if nums[0]<=target:
            dp[0][nums[0]] = True

        for i in range(1,n):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i]] if j-nums[i] >=0 else False)

        return dp[n-1][target]