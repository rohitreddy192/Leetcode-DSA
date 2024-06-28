class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        add_result = nums[0]
        sub_result = nums[0]

        for i in range(1, len(nums)):
            temp_add = max(add_result, sub_result) + nums[i]
            temp_sub = add_result - nums[i]

            add_result = temp_add
            sub_result = temp_sub

        return max(add_result, sub_result)