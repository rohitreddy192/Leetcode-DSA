class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        cars_2 = cars**2

        def isPossible(k):
            cnt = cars
            for rank in ranks:
                cnt -= int(math.sqrt(k/rank))
            return cnt<=0
            
        low = 1
        high = min(ranks)*(cars_2)
        ans = high
        while low<high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid
            else:
                low = mid + 1
        
        return ans