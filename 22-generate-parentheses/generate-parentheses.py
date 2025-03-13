class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(i,j,st):
            if i==n and j==n:
                ans.append(st)
                return 
            if i<j:
                return 
            
            if i<n:
                pickF = solve(i+1,j,st+"(")
            if i>j and j<n:
                pickB  = solve(i,j+1,st+")")

        solve(0,0,"")
        return ans
