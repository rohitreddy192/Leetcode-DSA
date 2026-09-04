class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def func(num):
            return (a*(num**2)) + (b*num) + c
        arr = []
        for num in nums:
            arr.append(func(num))
        
        return sorted(arr)