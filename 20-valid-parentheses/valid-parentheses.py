class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inp = "([{"
        oup = ")]}"
        for i in s:
            if len(stack)>0 and (i in oup and stack[-1]==inp[oup.index(i)]):
                stack.pop()
            else:
                stack.append(i)
        return True if len(stack)==0 else False