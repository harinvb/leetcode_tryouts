# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        res = 0
        while dq:
            w = len(dq)
            res = 0
            for _ in range(w):
                cur = dq.popleft()
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
                res += cur.val
        return res
