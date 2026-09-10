class Solution:
    def cherryPickup(self, a: List[List[int]]) -> int:
        n,m = len(a), len(a[0])
        dp = {}
        def solve(i,j1,j2):
            if j1<0 or j2<0 or j1>=m or j2>=m: return 0
            if i==n-1:
                if j1==j2:
                    return a[i][j1]
                else:
                    return a[i][j1] + a[i][j2]
            if (i,j1,j2) in dp: return dp[(i,j1,j2)]
            d1 = [-1,0,1]
            maxi = 0
            for jj1 in range(3):
                for jj2 in range(3):
                    dj1 = j1 + d1[jj1]
                    dj2 = j2 + d1[jj2]
                    if j1==j2:
                        maxi = max(a[i][j1]+solve(i+1,dj1,dj2),maxi)
                    else:
                        maxi = max(a[i][j1]+a[i][j2] + solve(i+1,dj1,dj2),maxi)
            dp[(i,j1,j2)] = maxi
            return dp[(i,j1,j2)]
        
        return solve(0,0,m-1)
