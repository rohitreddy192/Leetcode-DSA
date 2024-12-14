class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count_map = {0: 1}  # Initialize with 0 sum having 1 occurrence (base case)
        current_sum = 0
        result = 0
        
        for num in A:
            current_sum += num
            
            # Check how many times (current_sum - S) has occurred in the past
            result += count_map.get(current_sum - S, 0)
            
            # Update the map with the current_sum
            count_map[current_sum] = count_map.get(current_sum, 0) + 1
        
        return result