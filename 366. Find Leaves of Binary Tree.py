from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res: dict[List[int]] = defaultdict(list[int])

        def dfs(node: Optional[TreeNode]):
            if node is None: return 0
            my_idx = max(dfs(node.left), dfs(node.right))
            res[my_idx].append(node.val)
            return 1 + my_idx

        dfs(root)
        return list(res.values())
