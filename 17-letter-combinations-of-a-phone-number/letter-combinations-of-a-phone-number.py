class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        d=dict()
        d["2"] = "abc"
        d["3"] = "def"
        d["4"] = "ghi"
        d["5"] = "jkl"
        d["6"] = "mno"
        d["7"] = "pqrs"
        d["8"] = "tuv" 
        d["9"] = "wxyz"
        res = []
        def solve(idx, tmp):
            if idx==n:
                res.append(tmp)
                return
            for comb in d[digits[idx]]:
                solve(idx+1, tmp+comb)
            
        solve(0,"")
        return res
