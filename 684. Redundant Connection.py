from typing import List


class UnionFind:
    parent: List[int]
    rank: List[int]

    def __init__(self, size: int):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_a, node_b):
        parent_of_a = self.find(node_a)
        parent_of_b = self.find(node_b)

        if parent_of_a == parent_of_b:
            return False
        else:
            if self.rank[parent_of_a] >= self.rank[parent_of_b]:
                self.parent[parent_of_b] = parent_of_a
                self.rank[parent_of_a] += self.rank[parent_of_b]
            else:
                self.parent[parent_of_a] = parent_of_b
                self.rank[parent_of_b] += self.rank[parent_of_a]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redundant_edge = []
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                redundant_edge = edge
        return redundant_edge


print(Solution().findRedundantConnection(
    [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]))
