class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = list()
        candidates.sort()
        def solve(tot,j,l,ds):
            if tot == 0:
                l.append(tuple(ds))
                return
            for i in range(j,len(candidates)):
                if i!=j and candidates[i] == candidates[i-1]: continue
                if candidates[i]> tot: break
                ds.append(candidates[i])
                solve(tot-candidates[i],i+1,l,ds)
                ds.pop()
        solve(target,0,l,[])
        return l