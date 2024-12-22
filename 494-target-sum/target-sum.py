class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def solve(ind , target):
            if ind == 0: 
                if arr[0] == 0 and target==0: return 2
                elif target==0 or target==arr[0]: return 1
                return 0

            pick = 0
            
            if target-arr[ind]>=0: 
                pick = solve(ind-1,target-arr[ind])

            not_pick = solve(ind-1,target)

            return pick + not_pick

        n = len(arr)
        if n==1: return 1 if abs(arr[0])==abs(target) else 0
        totSum = sum(arr)
        if totSum - target < 0:
            return 0
        if (totSum - target) % 2 == 1:
            return 0
        return solve(n-1,(totSum-target)//2)