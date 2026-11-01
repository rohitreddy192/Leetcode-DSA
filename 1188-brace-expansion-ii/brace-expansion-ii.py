
class Solution:
    def braceExpansionII(self, expression: str):
        stack = []

        cur = {""}
        res = set()

        for ch in expression:

            if ch == "{":
                # Save the expression outside this brace.
                stack.append((cur, res))

                # Start evaluating the inner expression.
                cur = {""}
                res = set()

            elif ch == ",":
                # Finish the current alternative.
                res |= cur
                cur = {""}

            elif ch == "}":
                # Finish the current brace expression.
                res |= cur

                # Restore the previous expression.
                prev_cur, prev_res = stack.pop()

                # Concatenate outer expression with inner result.
                cur = {
                    a + b
                    for a in prev_cur
                    for b in res
                }

                res = prev_res

            else:
                # Concatenate the current letter.
                cur = {word + ch for word in cur}

        # Finish the top-level expression.
        res |= cur

        return sorted(res)
