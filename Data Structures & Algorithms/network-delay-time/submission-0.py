import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #[node] = [edge, cost]
        edgeMap = defaultdict(list)
        for u, v, t in times:
            edgeMap[u].append((v, t))
        
        visited = set()
        res = 0
        heap = [(0,k)]

        while heap:
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            time = weight

            for neighbor, cost in edgeMap[node]:
                heapq.heappush(heap, (weight + cost, neighbor ))
         
        if len(visited) == n:
            return time
        else:
            return -1
        

        

        
        