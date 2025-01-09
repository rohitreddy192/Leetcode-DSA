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

        return solve(n-1,totSum//2)