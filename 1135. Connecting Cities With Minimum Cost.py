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

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        min_weight = 0
        self.graph = [-1 for _ in range(n + 1)]
        connections = sorted(connections, key=lambda conn: conn[2])
        for conn in connections:
            if self.__union(conn[0], conn[1]): min_weight += conn[2]
        disconnected_components = 0
        for i in self.graph:
            if i == -1:
                disconnected_components += 1
                if disconnected_components > 2:
                    return -1
        return min_weight
