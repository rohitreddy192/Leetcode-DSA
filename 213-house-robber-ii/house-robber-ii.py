class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(start, i):
            if i<start: return 0
            pick = nums[i] + solve(start,i-2)
            not_pick = solve(start,i-1)
            return max(pick,not_pick)

        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        return max(solve(0,len(nums)-2), solve(1,len(nums)-1))