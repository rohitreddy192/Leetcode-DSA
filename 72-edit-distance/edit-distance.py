class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(i,j):
            # Check edge cases to end
            if i<0: return j+1
            if j<0: return i+1
            #Same character check
            same_char = 0
            operation_check = 0
            if word1[i]==word2[j]:
                same_char = solve(i-1,j-1)

            else:

                operation_check = min(1 + solve(i,j-1), 1 + solve(i-1,j), 1 + solve(i-1,j-1))
            
            return operation_check + same_char

        return solve(len(word1)-1, len(word2)-1)

