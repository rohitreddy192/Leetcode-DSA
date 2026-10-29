class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # count X in start and end --> should be the same
        if start.count('X') != end.count('X'):
            return False
        
        n = len(start)
        i = j = 0
        while (i < n and j < n):
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            # i and j are the indices representing the next
            # occurrences of non-X characters
            if i == n or j == n:
                return i == n and j == n

            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                #XL
                return False
            if start[i] == 'R' and i > j:
                #RX
                return False

            i += 1
            j += 1
     
        return True