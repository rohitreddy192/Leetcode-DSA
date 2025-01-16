class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sumCandy = sum(candies)
        n = len(candies)
        if sumCandy < k: return 0
        def isPossible(mid):
            if mid == 0: return True
            cnt = 0
            for candy in candies:
                cnt += candy // mid  
                if cnt >= k:  
                    return True
            return cnt >= k

        low = 0
        high = sum(candies)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans