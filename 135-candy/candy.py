class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n  # If only one child, they get one candy
        
        candies = [1] * n  # Every child gets at least one candy

        # Left-to-Right Pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:  
                candies[i] = candies[i - 1] + 1  

        # Right-to-Left Pass
        for i in range(n - 2, -1, -1):  
            if ratings[i] > ratings[i + 1]:  
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)  # Total candies required