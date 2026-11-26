class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for idx,num in enumerate(nums):
            if target-num in hm:
                return [hm[target-num],idx]
            hm[num] = idx
        
        return [-1,-1]