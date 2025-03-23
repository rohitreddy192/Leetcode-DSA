class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            """ Check if the string is a valid parentheses expression """
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        
        def backtrack(index, left_rem, right_rem, expr):
            """ Recursive function to remove invalid parentheses """
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    valid_string = "".join(expr)
                    if is_valid(valid_string):
                        result.add(valid_string)
                return
            
            char = s[index]
            expr.append(char)

            if char not in "()":  # Keep letters
                backtrack(index + 1, left_rem, right_rem, expr)
            else:
                if char == '(' and left_rem > 0:
                    expr.pop()
                    backtrack(index + 1, left_rem - 1, right_rem, expr)
                    expr.append(char)

                if char == ')' and right_rem > 0:
                    expr.pop()
                    backtrack(index + 1, left_rem, right_rem - 1, expr)
                    expr.append(char)

                backtrack(index + 1, left_rem, right_rem, expr)
            
            expr.pop()
        
        # Step 1: Find extra left & right parentheses to remove
        left_rem, right_rem = 0, 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()
        backtrack(0, left_rem, right_rem, [])
        return list(result)
