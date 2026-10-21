class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            stack = []
            for i in s:
                if i == ")":
                    if not stack:
                        return False
                    stack.pop()
                else:
                    if i=="(":
                        stack.append("(")
            
            return not stack

        res = set()
        n = len(s)
        @cache
        def solve(idx, st):
            if idx==n:
                if isValid(st):
                    res.add(st)
                return

            solve(idx+1, st+s[idx])
            solve(idx+1, st)

        solve(0,"")

        hp = defaultdict(list)
        minRemoved = float("inf")

        for st in res:
            removed = n - len(st)
            hp[removed].append(st)
            minRemoved = min(minRemoved, removed)

        return hp[minRemoved]