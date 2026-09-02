class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = len(s)-1
        j = len(g) - 1
        content = 0
        while i>=0 and j>=0:
            if s[i]<g[j]:
                j -= 1
            elif s[i]>=g[j]:
                i -= 1
                j -= 1
                content += 1
        return content