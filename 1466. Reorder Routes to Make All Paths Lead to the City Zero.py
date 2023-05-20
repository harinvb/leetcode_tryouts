from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """graph = defaultdict(list)
        roads = set()
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        res = 0

        def dfs(curr, parent):
            nonlocal res
            res += (parent, curr) in roads
            for ng in graph[curr]:
                if ng != parent:
                    dfs(ng, curr)

        dfs(0, -1)
        return res"""
        res = 0
        can_reach_zero = [False] * n
        can_reach_zero[0] = True
        while connections:
            next = []
            for i, j in connections:
                if can_reach_zero[i]:
                    can_reach_zero[j] = True
                elif can_reach_zero[j]:
                    can_reach_zero[i] = True
                    res += 1
                else:
                    next.append((i, j))
            connections = next
        return res


print(Solution().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
