from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    adj_list[i].append(j)

        def dfs(start: int, visited):
            for i in adj_list[start]:
                if i not in visited:
                    dfs(i, visited)

        final_res = -1
        for i in range(n):
            visited = {i}
            dfs(i, visited)
            final_res = max(final_res, len(visited))
        return final_res
