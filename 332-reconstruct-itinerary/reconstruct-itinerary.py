class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        # Step 1: Build adjacency list & sort destinations in reverse order
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        # Step 2: DFS traversal using Hierholzer's algorithm
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)

        dfs("JFK")
        
        # Step 3: Reverse the itinerary to get the correct order
        return itinerary[::-1]