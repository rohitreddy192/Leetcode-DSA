class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cnt = 0

        for ch in s:
            if ch == "(":
                cnt += 1
            elif ch == ")":
                if cnt == 0:
                    continue
                cnt -= 1

            stack.append(ch)

        ans = []
        for ch in reversed(stack):
            if ch == "(" and cnt > 0:
                cnt -= 1
                continue
            ans.append(ch)

        return "".join(reversed(ans))