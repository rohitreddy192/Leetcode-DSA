class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        bold = [False] * n   # mark which characters need bold
        
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)  # find next occurrence
        
        res = []
        i = 0
        while i < n:
            if bold[i]:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                res.append(s[i])
                i += 1
        
        return "".join(res)
