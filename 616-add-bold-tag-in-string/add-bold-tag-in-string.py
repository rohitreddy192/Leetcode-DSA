from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWord = True
        
        n = len(s)
        bold = [False] * n
        
        # Step 2: Use Trie to find matches
        for i in range(n):
            node = root
            j = i
            longest = -1
            while j < n and s[j] in node.children:
                node = node.children[s[j]]
                if node.isWord:
                    longest = j
                j += 1
            
            if longest != -1:
                for k in range(i, longest + 1):
                    bold[k] = True
        
        # Step 3: Build result
        res = []
        i = 0
        while i < n:
            if bold[i]:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                res.append(s[i])
                i += 1
        
        return "".join(res)
