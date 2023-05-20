from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        y = len(board)
        x = len(board[0])

        # k,l
        # k-1,l | k+1,l | k-1,l-1 | k-1,l+1 | k+1,l-1 | k+1,l-1 | k+1,l+1 | k-1 , l -1

        valid_boundary_value = lambda i, j: 1 if 0 <= i < y and 0 <= j < x and abs(board[i][j]) == 1 else 0
        for a in range(y):
            for b in range(x):
                neighbours = valid_boundary_value(a + 1, b) \
                             + valid_boundary_value(a - 1, b) \
                             + valid_boundary_value(a + 1, b + 1) \
                             + valid_boundary_value(a + 1, b - 1) \
                             + valid_boundary_value(a, b + 1) \
                             + valid_boundary_value(a, b - 1) \
                             + valid_boundary_value(a - 1, b - 1) \
                             + valid_boundary_value(a - 1, b + 1)
                if board[a][b]:
                    if neighbours < 2 or neighbours > 3:
                        board[a][b] = -1
                else:
                    if neighbours == 3: board[a][b] = 2
        for a in range(y):
            for b in range(x):
                if board[a][b] == -1:
                    board[a][b] = 0
                elif board[a][b] == 2:
                    board[a][b] = 1


s = Solution()
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
s.gameOfLife(board)
print(board)
