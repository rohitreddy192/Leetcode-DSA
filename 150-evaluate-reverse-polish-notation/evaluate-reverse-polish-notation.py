class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            if i in "+-*/":
                a, b = stack.pop(), stack.pop()
                if i == "+": stack.append(b+a)
                if i == "-": stack.append(b-a)
                if i == "*": stack.append(b*a)
                if i == "/": stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()
            