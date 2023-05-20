from collections import deque
from typing import List

MAX_COST = 10_00_01


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_matrix = [[-1] * n for _ in range(n)]
        for f, t, p in flights:
            adj_matrix[f][t] = p
        q = deque([(src, 0)])
        dist = [MAX_COST] * n
        stops_so_far = 0
        while q and stops_so_far <= k:
            l = len(q)
            for _ in range(l):
                cur, cost_so_far = q.popleft()
                for neighbour in range(n):
                    if adj_matrix[cur][neighbour] != -1 and dist[neighbour] > cost_so_far + adj_matrix[cur][neighbour]:
                        dist[neighbour] = cost_so_far + adj_matrix[cur][neighbour]
                        q.append((neighbour, dist[neighbour]))
            stops_so_far += 1
        return dist[dst] if dist[dst] != MAX_COST else -1


print(
    Solution().findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0,
                                 dst=3, k=1))
