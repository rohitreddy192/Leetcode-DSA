class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        print(cnt1)
        print(cnt2)
        print(chr(97+25))
        for i in range(0,26):
            tmp = chr(97+i)
            if tmp in cnt1 and tmp in cnt2:
                if abs(cnt1[tmp]-cnt2[tmp])>3:
                    return False
            elif tmp not in cnt1 and tmp not in cnt2:
                continue
            else:
                if tmp not in cnt1 and tmp in cnt2:
                    if cnt2[tmp]>3:
                        return False
                elif tmp not in cnt2 and tmp in cnt1:
                    if cnt1[tmp]>3:
                        return False
        
        return True