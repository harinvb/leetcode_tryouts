from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_map = defaultdict(set)
        for i in range(len(values)):
            a, b = equations[i]
            f, r = values[i], 1 / values[i]
            adj_map[a].add((f, b))
            adj_map[b].add((r, a))

        def dfs(start: str, target: str, visited: set[str]):
            if start == target:
                return True, 1
            visited.add(start)
            for nxt in adj_map[start]:
                if nxt[1] not in visited:
                    exists, nxt_res = dfs(nxt[1], target, visited)
                    if exists:
                        return True, nxt_res * nxt[0]
            visited.remove(start)
            return False, -1

        res_arr = []
        for a, b in queries:
            if a not in adj_map or b not in adj_map:
                res_arr.append(-1)
            else:
                res_arr.append(dfs(a, b, set())[1])
        return res_arr


print(Solution().calcEquation(equations=[["a", "b"]], values=[0.5],
                              queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
