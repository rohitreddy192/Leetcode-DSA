class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: Empty string is always breakable

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:  # If prefix is valid and suffix exists in wordSet
                    dp[i] = True
                    break  # No need to check further

        return dp[-1]