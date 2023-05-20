from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        res: List[int] = [-1] * N
        adj_lst = [[] for i in range(N)]

        for a, b in richer:
            adj_lst[b].append(a)

        def dfs(node) -> int:
            if res[node] == -1:
                res[node] = node
                for child in adj_lst[node]:
                    candidate_rich_and_quiet = dfs(child)
                    if quiet[candidate_rich_and_quiet] < quiet[res[node]]:
                        res[node] = candidate_rich_and_quiet
            return res[node]

        return list(map(dfs, range(N)))
