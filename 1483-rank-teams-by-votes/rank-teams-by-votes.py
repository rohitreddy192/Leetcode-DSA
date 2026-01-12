class Solution:

    def rankTeams(self, votes: List[str]) -> str:
        cnt = len(votes[0])
        ranks = {}
        for candidate in votes[0]:
            ranks[candidate] = [0] * cnt
        
        for vote in votes:
            for i, c in enumerate(vote):
                ranks[c][i] += 1
        
        print(ranks)
        res = sorted(ranks.keys())
        
        print(res)
        res.sort(key = ranks.get, reverse = True)
        
        print(res)
        return "".join(res)