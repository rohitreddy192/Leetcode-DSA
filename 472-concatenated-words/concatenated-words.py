class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)

        @lru_cache(None)
        def dfs(word):
            
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if((prefix in wordSet and suffix in wordSet) or
                    (prefix in wordSet and dfs(suffix))):
                    return True
            

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res