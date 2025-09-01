from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        output = []
        stack = []
        for num in heights[::-1]:
            cnt = 0
            while stack and stack[-1]<num:
                stack.pop()
                cnt += 1
            if stack:
                cnt += 1
            output.append(cnt)
            stack.append(num)
        return output[::-1]