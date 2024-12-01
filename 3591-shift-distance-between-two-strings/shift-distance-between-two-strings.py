class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        n = len(s)
        tc = 0
        for i in range(n):
            si = ord(s[i]) - ord('a')
            ti = ord(t[i]) - ord('a')
            fd = (ti - si) % 26
            bd = (si - ti) % 26
            fc = sum(nextCost[(si + j) % 26] for j in range(fd))
            bc = sum(previousCost[(si - j) % 26] for j in range(bd))
            tc += min(fc, bc)
        
        return tc
   