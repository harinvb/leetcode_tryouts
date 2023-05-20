from typing import List


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * n

    def find(self, node: int):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a == parent_b: return False
        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]
        return True


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for t, a, b in logs:
            if uf.union(a, b):
                n -= 1
            if n == 1:
                return t
        return -1
