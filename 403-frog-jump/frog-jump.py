class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)

        def jumpLists(k):
            return [k-1,k,k+1]

        @cache
        def solve(idx, jumpSize):
            if idx==n-1:
                return True

            curr_idx_val = stones[idx]

            isSolved = False
            for jump in jumpLists(jumpSize):
                for i in range(idx+1,n):
                    if curr_idx_val + jump == stones[i]:
                        isSolved = isSolved or solve(i,jump)
                        break
            
            return isSolved

                
        return solve(0,0)