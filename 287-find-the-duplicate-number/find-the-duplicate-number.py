class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Two-Three ways
        # 1. Sort and check for nums[i] == nums[i-1]
        # 2. HashMap to cnt 
        # 3. Checking for the overlap using the Linkedlist technique
        slow = nums[0]
        fast = nums[0]
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]    
            if slow == fast:
                fast = nums[0]
                while slow !=fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
