class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i, j, addOn = 0, 0, 0
        while i<n and j<m:
            if s[i]==t[j]:
                i += 1
                j += 1
            elif s[i]!=t[j]:
                if n>m:
                    i+=1
                elif m>n:
                    j += 1
                else:
                    i += 1
                    j += 1
                addOn += 1
        if i<n:
            return True if n-i==1 and addOn==0 else False
        if j<m:
            return True if m-j==1 and addOn==0 else False
        if addOn != 1:
            return False
        
        return True