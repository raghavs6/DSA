class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #
        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] == 'X' or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for c in range(COL):
            dfs(0, c)
            dfs(ROW - 1, c)
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL - 1)

        print(visited)

        for r in range(1, ROW):
            for c in range(1, COL):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'  