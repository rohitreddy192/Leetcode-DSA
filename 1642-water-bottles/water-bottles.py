class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        rem = numBottles
        while rem>0:
            rem = numBottles//numExchange
            ans += rem
            numBottles = rem + numBottles%numExchange
        
        return ans