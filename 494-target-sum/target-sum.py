class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:

        dp = {}
        def solve(idx, target):
            if idx<0: return 1 if target==0 else 0
            if (idx,target) in dp: return dp[(idx,target)]
            dp[(idx,target)] =  solve(idx-1, target-arr[idx]) + solve(idx-1, target+arr[idx])
            return dp[(idx,target)]
        return solve(len(arr)-1, target)

            