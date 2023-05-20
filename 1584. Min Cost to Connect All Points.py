from dataclasses import dataclass
from typing import List


class Solution:
    graph = []

    def __find(self, node):
        if self.graph[node] == -1:
            return node
        else:
            parent = self.__find(self.graph[node])
            self.graph[node] = parent
            return parent

    def __union(self, node_a, node_b):
        parent_a = self.__find(node_a)
        parent_b = self.__find(node_b)
        if parent_a == parent_b:
            return False
        else:
            self.graph[parent_a] = parent_b
            return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.graph = [-1 for _ in range(len(points))]
        min_weight = 0
        edges = []
        for i in range(0, len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        for each_edge in edges:
            if self.__union(each_edge[1], each_edge[2]):
                min_weight += each_edge[0]
        return min_weight
