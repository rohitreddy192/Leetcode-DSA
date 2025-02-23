from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            while st and st[-1]>0 and asteroid<0:
                if st[-1]<abs(asteroid):
                    st.pop()
                    continue
                elif st[-1]==abs(asteroid):
                    st.pop()
                break
            else:
                st.append(asteroid)
        return st