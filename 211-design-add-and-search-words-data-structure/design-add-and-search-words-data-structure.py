class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return node.isEndOfWord
        
        c = word[index]
        if c == ".":
            for child in node.children.values():
                if self._dfs(child, word, index + 1):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self._dfs(node.children[c], word, index + 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)