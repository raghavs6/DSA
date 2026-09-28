class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for src1, dst1, price in flights:
            adj[src1].append((dst1, price))

        q = [(0, src, 0)]

        while q:
            cost, city, flightsUsed = heapq.heappop(q)

            if city == dst:
                return cost

            if flightsUsed <= k:
                for nei, price in adj[city]:
                    newCost = cost + price
                    heapq.heappush(q, (newCost, nei, flightsUsed + 1))
        return - 1