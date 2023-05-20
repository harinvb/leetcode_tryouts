from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]
        rank = [1 for _ in range(4 * n * n)]

        def find(node: int) -> int:
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(a: int, b: int):
            parent_of_a = find(a)
            parent_of_b = find(b)
            if parent_of_a == parent_of_b:
                return False
            if rank[parent_of_a] > rank[parent_of_b]:
                parent[parent_of_b] = parent_of_a
                rank[parent_of_a] += rank[parent_of_b]
            else:
                parent[parent_of_a] = parent_of_b
                rank[parent_of_b] += rank[parent_of_a]
            return True

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                east = root + 0
                west = root + 3
                north = root + 2
                south = root + 1
                val = grid[r][c]
                if val != '\\':
                    union(east, south)
                    union(north, west)
                if val != '/':
                    union(east, north)
                    union(west, south)
                if r + 1 < n:
                    union(west, (root + 4 * n) + 0)
                if r - 1 >= 0:
                    union(east, (root - 4 * n) + 3)
                if c + 1 < n:
                    union(north, (root + 4) + 1)
                if c - 1 >= 0:
                    union(south, (root - 4) + 2)
        res = 0
        for i in range(4 * n * n):
            if find(i) == i:
                res += 1
        return res
