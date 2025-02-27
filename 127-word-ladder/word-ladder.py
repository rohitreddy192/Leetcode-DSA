class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque()
        que.append((beginWord,1))
        lenWord = len(beginWord)
        words = set(wordList)
        if beginWord in words: words.remove(beginWord)
        while que:
            word, steps = que.popleft()
            for i in 'abcdefghijklmnopqrstuvwxyz':
                for j in range(lenWord):
                    tempWord = word[:j]+i+word[j+1:]
                    if tempWord in words:
                        words.remove(tempWord)
                        if tempWord == endWord: 
                            return steps+1
                        que.append((tempWord, steps+1))
        return 0