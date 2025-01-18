class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left, right = 0, 0
        n = len(s)
        maxi = 0
        while right<n:
            seen[s[right]] += 1
            
            # If there are more than `k` distinct characters, shrink the window
            while len(seen) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            
            # Update the maximum length of the substring
            maxi = max(maxi, right - left + 1)
            
            # Move `right` pointer to the next character
            right += 1
        
        return maxi