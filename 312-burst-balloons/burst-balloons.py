class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        @cache
        def solve(i,j):
            if i>j: return 0
            maxi = 0
            for k in range(i,j+1):
                maxi = max(maxi, nums[i-1]*nums[k]*nums[j+1] + solve(i,k-1) + solve(k+1,j))
            
            return maxi

        return solve(1, n-2)