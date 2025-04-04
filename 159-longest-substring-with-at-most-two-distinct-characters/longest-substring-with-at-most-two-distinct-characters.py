class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = defaultdict(int)
        left, right = 0, 0
        n = len(s)
        maxi = 0
        while right<n and left<=right:
            if s[right] in seen or len(seen)<2:
                seen[s[right]] += 1
                right += 1
            else:
                while s[right] not in seen and len(seen)>=2:
                    seen[s[left]] -= 1
                    if seen[s[left]] == 0:
                        del seen[s[left]]
                    left += 1
            maxi = max(right-left,maxi)
        return maxi