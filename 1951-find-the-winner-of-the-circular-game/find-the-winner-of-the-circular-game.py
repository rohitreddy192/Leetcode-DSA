class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i for i in range(1,n+1)]
        i = 0
        while len(l)>1:
            n = len(l)
            l.pop((i+k-1)%n)
            i = (i+k-1)%n
        return l[0]