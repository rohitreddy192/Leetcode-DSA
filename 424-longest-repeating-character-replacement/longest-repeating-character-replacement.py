class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp = defaultdict(int)
        i,j,maxi = 0, 0, 0
        tmp = 0
        n = len(s)
        while j<n:
            mpp[s[j]] += 1
            tmp = max(tmp,mpp[s[j]])
            if not (j+1-i-tmp   <= k):
                mpp[s[i]] -= 1
                i += 1
            maxi = j+1-i
            j += 1
        return maxi