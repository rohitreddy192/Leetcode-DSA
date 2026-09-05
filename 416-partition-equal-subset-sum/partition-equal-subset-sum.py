class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum = sum(nums)
        halfSum = totSum//2
        if totSum%2!=0: return False

        dp = {}
        def solve(idx, target):
            if target==0: return True
            if target<0: return False

            if idx==0: return target==nums[0]

            if (idx,target) in dp: return dp[(idx,target)]
            dp[(idx,target)] =  solve(idx-1,target-nums[idx]) or solve(idx-1,target)

            return dp[(idx,target)]
        
        return solve(len(nums)-1, halfSum)
