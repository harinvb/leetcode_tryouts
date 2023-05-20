# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_map = defaultdict(list)

        def dfs(node: Optional[TreeNode]):
            if node.left:
                adj_map[node.val].append(node.left.val)
                adj_map[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adj_map[node.val].append(node.right.val)
                adj_map[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        current_depth = 0
        qu = deque([target.val])
        visited = set()
        while qu:
            if current_depth == k:
                return list(qu)
            cur_width = len(qu)
            for _ in range(cur_width):
                cur_node = qu.popleft()
                visited.add(cur_node)
                for i in adj_map[cur_node]:
                    if i not in visited:
                        qu.append(i)
            current_depth += 1
        return []
