class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        # m-> No. Of bouquets and k -> Number of flowers in each bouqet.
        # n -> Total number of flowers we have. 
        if m * k > n: return -1
        def isPossible(d):
            bouquets = 0
            consecutive = 0

            for flower in bloomDay:
                if flower <= d:
                    consecutive += 1

                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                else:
                    consecutive = 0

            return bouquets >= m


        low, high = min(bloomDay), max(bloomDay)
        ans = high
        while low<high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid
            else:
                low = mid + 1
        
        return ans