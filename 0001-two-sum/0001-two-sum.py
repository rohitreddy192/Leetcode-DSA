class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i,j in enumerate(nums):
            if target-j in hashMap:
                return [hashMap[target-j],i]
            hashMap[j] = i
        return [-1,-1]