from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:  # Collision occurs only when top is positive & asteroid is negative
                if st[-1] < abs(asteroid):  # Stack top is smaller, so it explodes
                    st.pop()
                    continue
                elif st[-1] == abs(asteroid):  # Both asteroids destroy each other
                    st.pop()
                break  # If stack top is larger, asteroid explodes

            else:  # If no collision occurs, push asteroid to stack
                st.append(asteroid)

        return st