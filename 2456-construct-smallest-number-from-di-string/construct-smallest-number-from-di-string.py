class Solution:
    def smallestNumber(self, s: str) -> str:
        res = []
        stack = []
        for i in range(len(s) + 1):
            stack.append(str(i + 1))
            if i == len(s) or s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        return ''.join(res)
