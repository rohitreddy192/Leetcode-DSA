class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, diff: int) -> bool:
        l = SortedList()
        for idx, num in enumerate(nums):
            # Get this idx
            # num + diff >= nums[i]
            right = bisect_right(l, num+diff)
            # Get this idx
            # num-diff <= nums[i]
            left = bisect_left(l,num-diff)
            print("Bisect Right", right)
            print("Bisect left", left)
            
                            
            l.add(num)

            if right > left:
                return True

            if len(l) > k:
                l.remove(nums[idx - k])

        
        return False