from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            a = stones[i]
            for j in range(i + 1, n):
                b = stones[j]
                if a[0] == b[0] or a[1] == b[1]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = [False] * n

        def dfs(node: int):
            visited[node] = True
            for i in adj_list[node]:
                if not visited[i]:
                    dfs(i)

        components = 0
        for cur_node in range(n):
            if not visited[cur_node]:
                components += 1
                dfs(cur_node)
        return n - components
