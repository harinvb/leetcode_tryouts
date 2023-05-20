from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        qu = deque()
        fresh_oranges = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    qu.append((i, j))

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        if not fresh_oranges:
            return 0
        time = -1
        while qu:
            w = len(qu)
            for _ in range(w):
                i, j = qu.popleft()
                for dir in directions:
                    p, q = i + dir[0], j + dir[1]
                    if is_valid(p, q) and grid[p][q] == 1:
                        grid[p][q] = 2
                        qu.append((p, q))
                        fresh_oranges -= 1
            time += 1
        return -1 if fresh_oranges else time
