class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        dp = {}
        def solve(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):  # Prune impossible cases early
                return False
            if (s1,s2) in dp: return dp[(s1,s2)]
            n = len(s1)
            for i in range(1, n):  # Try splitting at each index
                # Case 1: No swap (left-left and right-right comparison)
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    dp[(s1,s2)] = True
                    return True
                
                # Case 2: Swap (left-right and right-left comparison)
                if solve(s1[:i], s2[-i:]) and solve(s1[i:], s2[:-i]):
                    dp[(s1,s2)]= True
                    return True
            dp[(s1,s2)] = False
            return False
        
        return solve(s1, s2)
