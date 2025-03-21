class Solution:
    def frequencySort(self, s: str) -> str:
        t = Counter(s)
        t = sorted(t.items(), key=lambda kv: (-1*kv[1],kv[0]))
        str_return = ""
        for i in t:
            str_return += i[0]*i[1]
        return str_return