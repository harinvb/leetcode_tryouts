from typing import List

KNIGHT_MOVES = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        x = y = p = 0
        N = len(grid)
        final_p = (N ** 2) - 1
        while p != final_p:
            not_possible = True
            for move in KNIGHT_MOVES:
                nx, ny = x + move[0], y + move[1]
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == p + 1:
                    x, y, p = nx, ny, p + 1
                    not_possible = False
                    break
            if not_possible: return False
        return True


s = Solution()
print(s.checkValidGrid(
    [[24, 11, 22, 17, 4], [21, 16, 5, 12, 9], [6, 23, 10, 3, 18], [15, 20, 1, 8, 13], [0, 7, 14, 19, 2]]))
