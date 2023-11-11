class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = list()
        def solve(tot,i,l,ds):
            if tot<0: return
            if i>=len(candidates): return
            if tot == 0:
                l.append(tuple(ds))
                return
            ds.append(candidates[i])
            solve(tot-candidates[i],i,l,ds)
            ds.pop()
            solve(tot,i+1,l,ds)
        solve(target,0,l,[])
        return l