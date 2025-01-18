class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        def isPossible(mid):
            cnt = 0
            for i in range(1,n):
                noOfStations = (stations[i]-stations[i-1]) / mid
                cnt += math.ceil(noOfStations) - 1
            return cnt <= k

        low = 0
        high = 0
        for i in range(1,n):
            high = max(stations[i]-stations[i-1],high)
        
        while high-low > 1e-6:
            mid = (low+high)/2.0
            if isPossible(mid):
                high = mid
            else:
                low = mid
        return low
