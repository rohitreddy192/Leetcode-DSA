class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mpp = defaultdict(int)
        i, j, maxi = 0, 0, 0
        n = len(s)
        res = 0
        for j in range(n):
            mpp[s[j]] += 1
            
            while len(mpp) == 3:
                res += (n-j)
                mpp[s[i]] -= 1
                if mpp[s[i]] == 0:
                    del mpp[s[i]]
                i += 1
            
        return res
                