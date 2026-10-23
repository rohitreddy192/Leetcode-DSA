class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = Counter(p)
        counterS = defaultdict(int)
        trackerSet = set(counterP.keys())
        ans = []
        for jdx, st in enumerate(s):
            if st in trackerSet and Counter(s[jdx:jdx+len(p)]) == counterP:
                ans.append(jdx)
        
        return ans