class Solution:
    def rankTeams(self, votes):
        n = len(votes[0])

        # Count votes per position for each team
        count = {team: [0] * n for team in votes[0]}

        for vote in votes:
            for i, team in enumerate(vote):
                count[team][i] += 1

        # Sort teams using lambda
        teams = list(votes[0])
        teams.sort(
            key=lambda team: ([-count[team][i] for i in range(n)], team)
        )

        return "".join(teams)
