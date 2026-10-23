class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        

        logs.sort()
        parents = [x for x in range(n)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            
            return parents[x]
        
        def uunion(x,y):
            ua, ub = ufind(x), ufind(y)
            parents[ua] = ub


        cnt = 0
        for ts, x, y in logs:
            if ufind(x)!=ufind(y):
                uunion(x,y)
                cnt += 1

                if cnt==n-1:
                    return ts

            
        return -1