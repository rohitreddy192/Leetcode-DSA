class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()
        nums.sort(reverse=True)
        n = 0
        for num in nums:
            if num not in s:
                s.add(num)
                n += 1
                if n==3:
                    return num
        return max(nums)
            
