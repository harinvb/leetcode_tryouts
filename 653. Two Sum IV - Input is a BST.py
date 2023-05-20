# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None: return False
        return self.dfs_bs(root, k, set())

    def dfs_bs(self, root: Optional[TreeNode], target: int, seen: set[int]) -> bool:
        if root is None: return False
        if target - root.val in seen:
            return True
        seen.add(root.val)
        return self.dfs_bs(root.left, target, seen) or self.dfs_bs(root.right, target, seen)
