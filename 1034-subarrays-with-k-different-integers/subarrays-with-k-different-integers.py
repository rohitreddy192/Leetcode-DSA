class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
    
        def solve1(nums,k):
            n = len(nums)
            i = 0
            j = 0
            count = 0
            mp = defaultdict(int)
            while j<n:
                mp[nums[j]] += 1

                while len(mp) > k:
                    mp[nums[i]] -= 1
                    if mp[nums[i]] == 0:
                        del mp[nums[i]]
                    i += 1
                count += (j-i+1)
                j += 1

            print('*******')
            return count

        return solve1(s,k) - solve1(s,k-1)