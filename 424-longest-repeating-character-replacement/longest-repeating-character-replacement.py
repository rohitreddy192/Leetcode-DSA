class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        max_freq = 0
        start = 0
        max_length = 0

        for end in range(len(s)):
            # Increment the count of the current character
            freq_map[s[end]] += 1
            
            # Update the maximum frequency in the current window
            max_freq = max(max_freq, freq_map[s[end]])
            
            # If replacements required exceed k, shrink the window
            if (end - start + 1) - max_freq > k:
                freq_map[s[start]] -= 1  # Decrease the count of the outgoing character
                start += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, end - start + 1)
        
        return max_length