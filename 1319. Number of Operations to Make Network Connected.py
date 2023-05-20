from typing import List


class UnionFind:
    parent: List[int]
    rank: List[int]
    size: int

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.size = size

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)

        if parent_a == parent_b:
            return False
        else:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += self.rank[parent_b]
            else:
                self.parent[parent_a] = parent_b
                self.rank[parent_b] += self.rank[parent_a]
        return True

    def components(self):
        components = 0
        for i in range(self.size):
            if self.parent[i] == i: components += 1
        return components


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        excess_edges = 0
        uf = UnionFind(n)
        for a, b in connections:
            if not uf.union(a, b):
                excess_edges += 1
        components = uf.components()
        return components - 1 if components - 1 <= excess_edges else -1


print(Solution().makeConnected(100,
                               [[63, 95], [30, 57], [33, 97], [44, 60], [86, 96], [8, 86], [63, 79], [3, 60], [12, 92],
                                [70, 74], [15, 23], [10, 35], [49, 76], [14, 90], [48, 95], [19, 84], [14, 48],
                                [11, 15], [64, 72], [74, 93], [25, 29], [85, 97], [47, 61], [62, 64], [79, 91],
                                [16, 35], [83, 93], [93, 99], [17, 47], [14, 96], [23, 37], [28, 42], [1, 5], [48, 87],
                                [13, 30], [60, 65], [62, 80], [64, 69], [23, 51], [33, 49], [17, 97], [7, 25], [10, 33],
                                [6, 88], [3, 62], [97, 99], [60, 61], [55, 71], [11, 82], [31, 40], [29, 61], [25, 59],
                                [30, 43], [12, 54], [65, 80], [56, 61], [10, 24], [3, 93], [62, 78], [31, 86], [5, 65],
                                [20, 83], [43, 86], [11, 95], [34, 44], [95, 98], [3, 24], [8, 69], [43, 81], [52, 95],
                                [12, 29], [49, 65], [13, 29], [69, 91], [19, 47], [33, 71], [52, 80], [9, 57], [54, 65],
                                [45, 90], [1, 24], [44, 88], [38, 64], [49, 67], [12, 18], [7, 36], [28, 64], [60, 64],
                                [48, 77], [23, 95], [5, 15], [24, 62], [8, 78], [36, 65], [70, 80], [22, 24], [48, 59],
                                [23, 45], [81, 95], [18, 97], [26, 29], [37, 80], [26, 27], [25, 39], [62, 93],
                                [12, 56], [33, 75], [18, 48], [52, 57], [25, 94], [61, 87], [65, 89], [55, 86],
                                [12, 88], [34, 57], [8, 72], [12, 26], [27, 92], [84, 99], [45, 85], [7, 68], [1, 12],
                                [12, 53]]))
