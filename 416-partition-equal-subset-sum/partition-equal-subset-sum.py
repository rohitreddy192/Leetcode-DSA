class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        n = len(arr)
        sumArray = sum(arr)

        if sumArray%2!=0: return False

        @cache
        def solve(i, target):
            if target == 0: return True
            if target<0: return False
            if i<0: return target == 0

            return solve(i-1,target-arr[i]) or solve(i-1,target)

        return solve(n-1,sumArray//2)