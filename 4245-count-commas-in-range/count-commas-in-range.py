class Solution:
    def countCommas(self, n: int) -> int:
        #Split in chunks of 3
        if n<1000: return 0
        return n-999