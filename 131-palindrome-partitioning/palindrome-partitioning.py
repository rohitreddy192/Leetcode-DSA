class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(stri):
            return stri == stri[::-1]
        l = list()
        n = len(s)
        def solve(ind,path):
            if ind == n:
                l.append(tuple(path))
                return
            for i in range(ind,n):
                if(isPalindrome(s[ind:i+1])):
                    path.append(s[ind:i+1])
                    solve(i+1,path)
                    path.pop()
        solve(0,[])
        return l