class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)

        for src1, dst1, price in flights:
            adj[src1].append((dst1, price))

        # (cost, city, flightsUsed)
        q = [(0, src, 0)]

        # cheapest cost for a particular:
        # (city, flightsUsed)
        best = {(src, 0): 0}

        while q:
            cost, city, flightsUsed = heapq.heappop(q)

            # Ignore an outdated expensive version
            if cost > best[(city, flightsUsed)]:
                continue

            if city == dst:
                return cost

            # k stops means at most k + 1 flights
            if flightsUsed <= k:
                for nei, price in adj[city]:
                    newCost = cost + price
                    newFlights = flightsUsed + 1

                    state = (nei, newFlights)

                    if newCost < best.get(state, float("inf")):
                        best[state] = newCost
                        heapq.heappush(
                            q,
                            (newCost, nei, newFlights)
                        )

        return -1