# Definition for a Node.
from collections import deque
from typing import Any


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> Any | None:
        if node is None: return None
        visited_node_map = {}
        q = deque([node])
        visited_node_map[node] = Node(node.val)
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                for ne in cur.neighbors:
                    if ne not in visited_node_map:
                        visited_node_map[ne] = Node(ne.val)
                        q.append(ne)
                    visited_node_map[cur].neighbors.append(visited_node_map[ne])
        return visited_node_map[node]


print('hit' - 'hot')
