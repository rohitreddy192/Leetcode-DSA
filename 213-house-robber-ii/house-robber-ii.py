class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}
        def solve(baseIdx, idx):
            if idx < baseIdx: return 0
            if (baseIdx,idx) in dp: return dp[(baseIdx,idx)]

            pick = nums[idx] + solve(baseIdx, idx-2)
            not_pick = solve(baseIdx, idx-1)

            dp[(baseIdx,idx)] =  max(pick, not_pick)

            return dp[(baseIdx,idx)]
        if len(nums)<=2: return max(nums)
        return max(solve(0, len(nums)-2), solve(1,len(nums)-1))