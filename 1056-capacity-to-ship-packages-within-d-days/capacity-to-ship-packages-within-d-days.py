class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(k):
            tot = 1
            consec = 0
            for i in weights:
                if i+consec <= k:
                    consec += i
                else:
                    consec = i
                    tot += 1
            
            return tot <= days

        low, high = max(weights), sum(weights)

        while low<high:
            mid = (low+high)//2
            if isPossible(mid):
                high = mid
            else:
                low = mid+1
        
        return low