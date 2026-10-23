class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = Counter(p)
        trackerSet = set(counterP.keys())
        ans = []
        m = len(p)

        for jdx, st in enumerate(s):
            if jdx + m <= len(s) and st in trackerSet:
                if Counter(s[jdx:jdx + m]) == counterP:
                    ans.append(jdx)

        return ans