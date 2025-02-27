class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required = Counter(t)  # Frequency of chars in t
        total = len(required)  # Unique chars needed

        # Sliding window pointers
        i, j = 0, 0
        found = 0  # Count of unique chars that match required frequency
        founded = defaultdict(int)

        # Variables to track the minimum window
        mini = float("inf")
        minii = ""

        while j < len(s):
            # Expand window by including s[j]
            if s[j] in required:
                founded[s[j]] += 1
                if founded[s[j]] == required[s[j]]:
                    found += 1
            
            # Contract window when valid
            while found == total:
                if j - i + 1 < mini:
                    mini = j - i + 1
                    minii = s[i:j + 1]

                # Try to shrink from the left
                if s[i] in required:
                    if founded[s[i]] == required[s[i]]:
                        found -= 1  # No longer valid window
                    founded[s[i]] -= 1

                i += 1  # Move left pointer

            j += 1  # Expand right pointer

        return minii
