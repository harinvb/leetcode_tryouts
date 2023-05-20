from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        adj_lst = [[] for _ in range(N)]
        for a, b in edges:
            adj_lst[a].append(b)
            adj_lst[b].append(a)

        def farthest_node(node, visited):
            max_h = 0
            far_node = node
            visited[node] = True
            for child in adj_lst[node]:
                if not visited[child]:
                    h, child_farthest_node = farthest_node(child, visited)
                    if h > max_h:
                        far_node = child_farthest_node
                        max_h = h
            visited[node] = False
            return 1 + max_h, far_node

        _, start = farthest_node(0, [False for _ in range(N)])
        depth, _ = farthest_node(start, [False for _ in range(N)])

        return depth - 1


print(Solution().treeDiameter([[0, 1], [0, 2]]))
