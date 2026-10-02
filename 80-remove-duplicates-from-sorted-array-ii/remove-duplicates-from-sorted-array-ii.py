class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        d = defaultdict(int)
        for idx, num in enumerate(nums):
            if d[num]>=2:
                d[num] += 1
                continue
                
            d[num] += 1
            new_nums.append(num)
        
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return len(new_nums)