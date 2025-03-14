class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        tot = sum(arr)
        if tot%2==1: return False

        dp = {}
        def solve(i,t):
            if t==0: return True
            if i==0: return arr[0]==t

            if (i,t) in dp: return dp[(i,t)]
            dp[(i,t)] = solve(i-1,t) or (solve(i-1,t-arr[i]) if arr[i]<=t else False)

            return dp[(i,t)]
        
        return solve(len(arr)-1,tot//2)