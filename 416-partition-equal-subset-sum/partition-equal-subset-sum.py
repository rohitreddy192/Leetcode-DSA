class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum = sum(nums)
        if totSum%2!=0: return False

        n = len(nums)

        @lru_cache(None)
        def solve(i,target):
            if target==0: return True
            if target<0: return False
            if i==0:
                return nums[0]==target
            return solve(i-1,target) or solve(i-1,target-nums[i])

        # return solve(n-1,totSum//2)
        halfSum = totSum//2
        dp = [[False for i in range(halfSum+1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        if nums[0]<=halfSum:
            dp[0][nums[0]] = True

        for i in range(1,n):
            for j in range(1,halfSum+1):
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-nums[i]] if j-nums[i]>=0 else False)

        return dp[n-1][halfSum]