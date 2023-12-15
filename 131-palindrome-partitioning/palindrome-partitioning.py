class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(temp):
            return temp==temp[::-1]
        def solve(ind, ds, ans):
            if ind==len(s):
                ans.append(tuple(ds))
            
            for i in range(ind, len(s)):
                if isPalindrome(s[ind:i+1]):
                    ds.append(s[ind:i+1])
                    solve(i+1, ds, ans)
                    ds.pop()
        ans = []
        solve(0, [], ans)
        return ans