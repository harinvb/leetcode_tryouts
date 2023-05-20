import sys
from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2 or edges[node1] == node2 or edges[node2] == node1:
            return min(node2, node1)
        l = len(edges)
        qu = deque()
        qu.append(node1)
        qu.append(node2)
        visited = [False] * l
        visited[node1] = True
        visited[node2] = True
        res = sys.maxsize
        while qu:
            w = len(qu)
            are_paths_merging = False
            for _ in range(w):
                cur = qu.popleft()
                neighbour = edges[cur]
                if neighbour != -1:
                    if visited[neighbour]:
                        res = min(neighbour, res)
                        are_paths_merging = True
                    qu.append(neighbour)
                    visited[neighbour] = True
            if are_paths_merging:
                return res
        return -1
