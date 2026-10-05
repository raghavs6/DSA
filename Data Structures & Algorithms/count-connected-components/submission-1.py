class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adjList = {}

        for i in range(n):
            adjList[i] = []

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = set()

        def dfs(i):
            if i in visit:
                return

            visit.add(i)

            for nei in adjList[i]:
                dfs(nei)

        res = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res