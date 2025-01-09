class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if i != "#":
                s1.append(i)
            else:
                if len(s1)>0:
                    s1.pop()
        
        for j in t:
            if j != "#":
                s2.append(j)
            else:
                if len(s2)>0:
                    s2.pop()

        s = "".join(s1)
        t = "".join(s2)
        return s==t