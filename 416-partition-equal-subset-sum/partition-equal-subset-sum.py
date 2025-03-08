class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        totSum = sum(arr)
        if totSum%2!=0: return False

        n = len(arr)
        target = totSum//2
        dp = {}
        def solve(i,target):
            if target==0: return True
            if i==0: return arr[0]==target
            if (i,target) in dp: return dp[(i,target)]
            dp[(i,target)] = solve(i-1,target-arr[i]) or solve(i-1,target)
            return dp[(i,target)]
        
        return solve(len(arr)-1,target)