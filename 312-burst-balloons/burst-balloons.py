class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @lru_cache(None)
        def solve(i,j):
            if i>j: return 0

            max_cost = -1e9
            for k in range(i,j+1):
                cost = (nums[i-1] * nums[k] * nums[j+1]) + solve(i,k-1) + solve(k+1,j)
                max_cost = max(max_cost, cost)
            
            return max_cost
        return solve(1,len(nums)-2)