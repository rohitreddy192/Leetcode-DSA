class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        ans = []
        n = len(candidates)
        def solve(idx, tmp, target):
            if target == 0:
                ans.append(tmp.copy())
                return 
            if idx==n: return 

            solve(idx+1, tmp, target)
            if target-candidates[idx]>=0:
                tmp.append(candidates[idx])
                solve(idx, tmp, target-candidates[idx])
                tmp.pop()
        
        solve(0, [], target)
        return ans