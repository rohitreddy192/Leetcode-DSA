class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def isPossible(k):
            ans = 0
            for i in range(n):
                ans += math.ceil(piles[i]/k)
            return ans<=h

        low, high = 1, max(piles)

        ans = high
        while low<high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid
            else:
                low = mid+1
        return ans