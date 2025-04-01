class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == len(weights): return 0
        
        sorted_w = []
        for i in range(len(weights)-1):
            sorted_w.append(weights[i]+weights[i+1])
        
        sorted_w.sort()

        print(sorted_w)
        return sum(sorted_w[::-1][:k-1]) - sum(sorted_w[:k-1])