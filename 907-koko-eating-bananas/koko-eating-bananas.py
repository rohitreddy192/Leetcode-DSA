class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(val):
            return sum(ceil(x/val) for x in piles) <= h

        start, end = 1, max(piles)
        ans = end
        while start<=end:
            val = (start+end)//2
            if isPossible(val):
                ans = val
                end = val - 1
            else:
                start = val + 1
        
        return ans