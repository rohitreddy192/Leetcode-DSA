class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def solve(i,j):
            if i>j: return 0

            cnt = float("-inf")

            for k in range(i,j+1):
                coins = nums[i-1]*nums[k]*nums[j+1] + solve(i,k-1) + solve(k+1,j)
                cnt = max(cnt,coins )

            
            return cnt

        return solve(1,len(nums)-2)