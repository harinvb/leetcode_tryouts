from typing import List


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        pA = self.find(a)
        pB = self.find(b)
        if pA == pB:
            return False
        elif self.rank[pA] > self.rank[pB]:
            self.rank[pA] += self.rank[pB]
            self.parent[pB] = self.parent[pA]
        else:
            self.rank[pB] += self.rank[pA]
            self.parent[pA] = self.parent[pB]
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union_find.union(i, j)
        components = set()
        for i in range(1, n):
            components.add(union_find.find(i))
        return len(components)
