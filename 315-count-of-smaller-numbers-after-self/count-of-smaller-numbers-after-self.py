class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        op = []
        for n in nums[::-1]:
            ans = SortedList.bisect_left(s,n)
            op.append(ans)
            s.add(n)
        
        return op[::-1]