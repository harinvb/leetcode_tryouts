# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cur_level = [(root, 1)]
        res = 0
        while cur_level:
            next_level = []
            res = max(res, cur_level[-1][1] - cur_level[0][1] + 1)
            for node, number in cur_level:
                if node.left:
                    next_level.append((node.left, 2 * number))
                if node.right:
                    next_level.append((node.right, 2 * number + 1))
            cur_level = next_level
        return res
