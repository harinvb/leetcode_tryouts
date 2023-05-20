from typing import List


class UnionFind:
    def __init__(self, size) -> None:
        self.group = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, person: int) -> int:
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, person_1: int, person_2: int) -> bool:
        group_1 = self.find(person_1)
        group_2 = self.find(person_2)
        if group_1 == group_2:
            return False
        if self.rank[group_1] > self.rank[group_2]:
            self.group[group_2] = group_1
        elif self.rank[group_1] < self.rank[group_2]:
            self.group[group_1] = group_2
        else:
            self.group[group_1] = group_2
            self.rank[group_2] += 1

        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        # add the virtual vertex (index with 0) along with the new edges.
        ordered_edges += [(cost, 0, node + 1) for node, cost in enumerate(wells)]

        # add the existing edges
        ordered_edges += [(cost, node_a, node_b) for node_a, node_b, cost in pipes]

        # sort the entire edges by their weights
        ordered_edges.sort()

        # iterate through the ordered edges
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_1, house_2 in ordered_edges:
            # determine if we should add the new edge to the final MST
            if uf.union(house_1, house_2):
                total_cost += cost

        return total_cost
