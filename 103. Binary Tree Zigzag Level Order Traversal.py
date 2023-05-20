# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res: List[List[int]] = []

        qu = deque()
        qu.append(root)
        level_reverse = False
        while qu:
            cur_level = []
            level = len(qu)
            for _ in range(level):
                node = qu.popleft()
                cur_level.append(node.val)
                if node.left is not None: qu.append(node.left)
                if node.right is not None: qu.append(node.right)
            if level_reverse:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level)
            level_reverse = not level_reverse
        return res
