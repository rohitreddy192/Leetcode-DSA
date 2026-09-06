class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()
        dq.append((beginWord,1))
        words = set(wordList)
        if endWord not in words: return 0
        while dq: #5000
            node, steps = dq.popleft()
            for i in range(97, 97+27): #27
                ch = chr(i)
                for j in range(len(node)): #10
                    newWord = node[:j]+ch+node[j+1:]
                    if newWord in words:
                        dq.append((newWord, steps+1))
                        words.remove(newWord)
                    if newWord == endWord:
                        return steps+1
        
        return 0
