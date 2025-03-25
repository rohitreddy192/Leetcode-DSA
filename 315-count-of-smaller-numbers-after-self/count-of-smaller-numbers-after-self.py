class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = []
        op = []
        for n in nums[::-1]:
            ans = bisect_left(s,n)
            op.append(ans)
            if ans == len(s):
                s.append(n)
            else:
                s.insert(ans,n)
        
        return op[::-1]