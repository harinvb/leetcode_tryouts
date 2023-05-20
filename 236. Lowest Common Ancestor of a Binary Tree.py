# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = TreeNode(0)

        def recurse(node: TreeNode) -> bool:
            if not node: return False
            left = recurse(node.left)
            right = recurse(node.right)
            mid = node == p or node == q
            if left + mid + right >= 2:
                nonlocal lca
                lca = node
            return left or mid or right

        recurse(root)
        return lca
