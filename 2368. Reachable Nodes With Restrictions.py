from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        visited = [False] * n
        for i in restricted:
            visited[i] = True

        def dfs(node: int):
            res = 1
            visited[node] = True
            for neighbour in adj_map[node]:
                if not visited[neighbour]:
                    res += dfs(neighbour)
            return res

        return dfs(0)
