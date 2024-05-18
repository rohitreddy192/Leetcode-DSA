class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        def func(ind, target, ds, ans):
            if target == 0:
                ans.append(tuple(ds))
                return 
            for i in range(ind, len(arr)):
                if i!=ind and arr[i-1]==arr[i]: continue
                if target<arr[i]: break
                ds.append(arr[i])
                func(i+1,target-arr[i],ds,ans)
                ds.pop()
        ans = []
        func(0,target,[], ans)
        return ans
