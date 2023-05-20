from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[False] * n for _ in range(n)]
        for a, b in roads:
            adj_list[a][b] = True
            adj_list[b][a] = True
        degree = [(sum(adj_list[i]), i) for i in range(n)]
        res = 0
        for i in range(n):
            r1, n1 = degree[i]
            for j in range(i + 1, n):
                r2, n2 = degree[j]
                cur = r1 + r2
                if adj_list[n1][n2] or adj_list[n2][n1]:
                    cur -= 1
                res = max(res, cur)
        return res


print(Solution().maximalNetworkRank(n=2, roads=[]))
