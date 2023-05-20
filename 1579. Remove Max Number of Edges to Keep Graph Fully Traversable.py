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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Union find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        extra_edges = alice_edges = bob_edges = 0

        # Alice and Bob
        root = [i for i in range(n + 1)]
        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    alice_edges += 1
                    bob_edges += 1
                else:
                    extra_edges += 1
        both = root[:]

        # only Alice
        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    alice_edges += 1
                else:
                    extra_edges += 1

        # only Bob
        root = both
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    bob_edges += 1
                else:
                    extra_edges += 1

        return extra_edges if alice_edges == bob_edges == n - 1 else -1


sol = Solution()
print(sol.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
