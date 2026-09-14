class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return 
            cur = grid[r][c]
            if cur == "0":
                return 
            if (r,c) in visited:
                return 
            visited.add((r,c))
            
            dfs(r - 1, c)
            dfs(r + 1,c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1

                dfs(r,c)
        return islands

                


