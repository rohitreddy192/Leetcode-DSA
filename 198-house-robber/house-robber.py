class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            if i<0: return 0
            pick = nums[i] + solve(i-2)
            not_pick = solve(i-1)
            return max(pick, not_pick)
        return solve(len(nums)-1)