class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count_map = {0: 1}  
        current_sum = 0
        result = 0
        
        for num in A:
            current_sum += num
            
            result += count_map.get(current_sum - S, 0)
            
            count_map[current_sum] = count_map.get(current_sum, 0) + 1
        
        return result