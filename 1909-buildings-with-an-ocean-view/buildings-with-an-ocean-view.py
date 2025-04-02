class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        mini = heights[-1]
        res = []
        res.append(n-1)
        for i in range(n-2,-1,-1):
            if heights[i]>mini:
                res.append(i)
                mini = max(mini, heights[i])
        return res[::-1]