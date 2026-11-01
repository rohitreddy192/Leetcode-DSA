class Solution:
    def braceExpansionII(self, expression: str):
        operators = []
        operands = []

        def apply():
            op = operators.pop()
            b = operands.pop()
            a = operands.pop()

            if op == ',':
                operands.append(list(set(a) | set(b)))
            else:
                # Cartesian product
                operands.append([x + y for x in a for y in b])

        def precedence(op):
            return 2 if op == '*' else 1

        def add_operator(op):
            while (operators and operators[-1] != '{'
                   and precedence(operators[-1]) >= precedence(op)):
                apply()
            operators.append(op)

        prev = None

        for ch in expression:

            if ch.isalpha():
                # Implicit concatenation
                if prev in ('letter', 'close'):
                    add_operator('*')

                operands.append([ch])
                prev = 'letter'

            elif ch == '{':
                if prev in ('letter', 'close'):
                    add_operator('*')

                operators.append('{')
                prev = 'open'

            elif ch == ',':
                add_operator(',')
                prev = 'comma'

            elif ch == '}':
                while operators and operators[-1] != '{':
                    apply()

                operators.pop()
                prev = 'close'

        while operators:
            apply()

        return sorted(set(operands[-1]))