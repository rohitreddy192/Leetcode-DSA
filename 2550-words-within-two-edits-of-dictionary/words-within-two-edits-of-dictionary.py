class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        ans = []

        for word in queries:

            for dict_word in dictionary:

                edits = 0

                for i in range(len(word)):
                    if word[i] != dict_word[i]:
                        edits += 1

                if edits <= 2:
                    ans.append(word)
                    break

        return ans