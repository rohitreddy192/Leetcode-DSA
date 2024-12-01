class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        k = n//k
        return Counter(s[i:i+k] for i in range(0,n,k)) == Counter(t[i:i+k] for i in range(0,n,k))