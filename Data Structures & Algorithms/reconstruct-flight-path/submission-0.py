import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for fromAir, toAir in tickets:
            heapq.heappush(graph[fromAir], toAir)
        
        res = []

        def dfs(airport):
            while graph[airport]:
                nextAir = heapq.heappop(graph[airport])
                dfs(nextAir)
            
            res.append(airport)

        dfs("JFK")
        
        res.reverse()

        return res
