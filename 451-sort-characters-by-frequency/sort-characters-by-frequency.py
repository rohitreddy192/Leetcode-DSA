class Solution:
    def frequencySort(self, s: str) -> str:
        t = Counter(s)
        t = sorted(t.items(), key=lambda kv: kv[1] , reverse=True)
        str_return = ""
        for i in t:
            str_return += i[0]*i[1]
        return str_return