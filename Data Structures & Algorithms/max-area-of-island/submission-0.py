class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = []
        max_val = 0
        visited = set()
        area = 0


        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return 0
            cell = grid[r][c]

            if (r,c) in visited:
                return 0
            if cell == 0:
                return 0
            visited.add((r,c))
            if cell == 1:
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
                



            
            

        for r in range(ROW):
            for c in range(COL):
                area = dfs(r, c)
                max_val = max(max_val, area)
        return max_val



        