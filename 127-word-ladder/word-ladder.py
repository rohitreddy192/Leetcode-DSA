class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words: return 0

        dq = deque()
        dq.append((beginWord, 1))
        
        n = len(beginWord)
        while dq:
            word, steps = dq.popleft()
            for i in range(n):
                for k in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+k+word[i+1:]
                    if newWord in words:
                        dq.append((newWord,steps+1))
                        words.remove(newWord)
                    if newWord == endWord:
                        return steps + 1
        
        return 0