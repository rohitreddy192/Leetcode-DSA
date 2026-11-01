class Solution:
    def longestPrefix(self, s: str) -> str:
        # Longest Common Lets see starting with s[0] and its indices

        if not s: return ""

        idx0 = s[0]
        n = len(s)
        l = list()
        for idx, st in enumerate(s):
            if st == idx0 and idx!=0:
                l.append(idx)

        for idx in l:
            le = n - idx
            prefix = s[:le]
            suffix = s[idx:]
            # print(prefix)
            # print(suffix)
            if prefix==suffix:
                return prefix

        return ""