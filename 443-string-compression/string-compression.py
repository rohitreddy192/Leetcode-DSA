class Solution:
    def compress(self, chars: List[str]) -> int:
        l = list()
        i,j = 0, 0
        n = len(chars)
        while i<n:
            while j<n and chars[i]==chars[j]:
                j += 1
            l.append(chars[i])
            tmp = (j-i)
            tmpAns = []
            if tmp>1:
                while tmp>=10:
                    rem = tmp%10
                    tmpAns.append(str(rem))
                    tmp = tmp//10
                if tmp >= 1:
                    tmpAns.append(str(tmp))
                if tmpAns:
                    l.extend(tmpAns[::-1])
                
            if i==j:
                i += 1
            else:
                i = j
        for i in range(min(n,len(l))):
            chars[i] = l[i]
        return len(l)