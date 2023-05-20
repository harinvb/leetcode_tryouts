# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """nodes: List[Optional[TreeNode]] = []

        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        nodes.append(None)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]"""

        # in-place

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            if node.right is None and node.left is None:
                return node
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail is not None:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return left_tail if right_tail is None else right_tail

        dfs(root)
