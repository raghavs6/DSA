class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        
        
        
        mapEdge = {}
        visited = set()

        for i in range(n):
            mapEdge[i] = []
        for node, edge in edges:
            mapEdge[node].append(edge)
            mapEdge[edge].append(node)
        
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in mapEdge[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

                
