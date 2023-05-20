from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # replace to be converted to o with y
        m = len(board)
        n = len(board[0])

        def dfs(x: int, y: int):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == 'X' or board[x][y] == 'T':
                return
            board[x][y] = 'T'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m - 1][i] == 'O':
                dfs(m - 1, i)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
