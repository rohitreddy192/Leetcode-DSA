class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(opened, closed, temp):
            if opened>closed:
                return 
            if opened==0 and closed==0:
                ans.append(temp)
            if opened>0:
                solve(opened-1, closed, temp+"(")
            if closed>0 and closed>opened:
                solve(opened, closed-1, temp+")")

        solve(n,n,"")

        return ans