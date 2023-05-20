from typing import List

NEIGHBOURS = ((0, 1), (1, 0), (-1, 0), (0, -1))


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[-1] * n for _ in range(m)]
        cur_set = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    cur_set.add((i, j))
        cur_fill_val = 0
        while len(cur_set) != 0:
            nxt_set = set()
            for x, y in cur_set:
                res[x][y] = cur_fill_val
            for x, y in cur_set:
                for a, b in NEIGHBOURS:
                    i = x + a
                    j = y + b
                    if 0 <= i < m and 0 <= j < n and res[i][j] == -1:
                        nxt_set.add((i, j))
            cur_fill_val += 1
            cur_set = nxt_set
        return res


print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
