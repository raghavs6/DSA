class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create maxHeap
        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if y < x:
                res = x - y
                heapq.heappush(stones, -res)
            
        if len(stones) == 0:
            return 0
        return -stones[0]



