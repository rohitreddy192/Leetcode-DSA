
class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        opStack = []

        def doOp(a, b, op):
            if op == "+":
                return a + b
            return a - b

        i = 0
        n = len(s)

        while i < n:
            ch = s[i]

            if ch == " ":
                i += 1
                continue

            if ch.isdigit():
                num = 0

                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                numStack.append(num)
                continue

            if ch == "(":
                opStack.append(ch)

            elif ch == ")":
                while opStack and opStack[-1] != "(":
                    op = opStack.pop()
                    b = numStack.pop()
                    a = numStack.pop()
                    numStack.append(doOp(a, b, op))

                if opStack:
                    opStack.pop()

            else:  # + or -
                # Find the previous non-space character
                prev = i - 1
                while prev >= 0 and s[prev] == " ":
                    prev -= 1

                # Handle unary signs: -2, (-2), 1 - (-2)
                if prev < 0 or s[prev] in "(+-":
                    numStack.append(0)

                # Evaluate pending operators
                while opStack and opStack[-1] != "(":
                    op = opStack.pop()
                    b = numStack.pop()
                    a = numStack.pop()
                    numStack.append(doOp(a, b, op))

                opStack.append(ch)

            i += 1

        while opStack:
            op = opStack.pop()
            b = numStack.pop()
            a = numStack.pop()
            numStack.append(doOp(a, b, op))

        return numStack[-1]
