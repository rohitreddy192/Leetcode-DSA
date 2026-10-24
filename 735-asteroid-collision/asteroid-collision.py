
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        def isSameDirection(a, b):
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                return False
            return True

        def resultAfterCollision(a, b):
            c, d = abs(a), abs(b)
            if c > d:
                return a
            elif c < d:
                return b
            else:
                return 0

        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and not isSameDirection(stack[-1], asteroid):
                # Only right-moving and then left-moving asteroids collide
                if stack[-1] < 0 or asteroid > 0:
                    break

                stackTop = stack.pop()
                res = resultAfterCollision(stackTop, asteroid)

                if res == stackTop:
                    stack.append(stackTop)
                    alive = False
                    break

                if res == 0:
                    alive = False
                    break

                # Incoming asteroid survives; continue checking the stack

            if alive:
                stack.append(asteroid)

        return stack
