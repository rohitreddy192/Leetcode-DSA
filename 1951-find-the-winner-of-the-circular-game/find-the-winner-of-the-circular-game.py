class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i for i in range(1,n+1)]
        i = 0
        while n>1:
            l.pop((i+k-1)%n)
            i = (i+k-1)%n
            n = len(l)
        return l[0]