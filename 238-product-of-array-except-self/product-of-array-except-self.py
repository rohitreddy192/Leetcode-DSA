class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Left = [1 for i in range(n)]
        Right = [1 for i in range(n)]
        for i in range(1,n):
            Left[i]  = Left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            Right[i] = Right[i+1]*nums[i+1]
        for i in range(n):
            Left[i] = Left[i]*Right[i]
        return Left