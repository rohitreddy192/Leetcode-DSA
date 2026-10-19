class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)

        def jumpLists(k):
            return [k-1,k,k+1]

        def solve(idx, jumpSize, dp):
            if idx==n-1:
                return True

            if (idx,jumpSize) in dp: return dp[(idx,jumpSize)]
            isSolved = False
            for jump in jumpLists(jumpSize):
                for i in range(idx+1,n):
                    if stones[idx] + jump == stones[i]:
                        isSolved = isSolved or solve(i,jump,dp)
                        break
            
            dp[(idx,jumpSize)] = isSolved
            return isSolved
                
        return solve(0,0,{})