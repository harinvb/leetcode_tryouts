# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        final_res = 0

        def dfs(node: TreeNode):
            if node is None: return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            if node.val % 2 == 0:
                nonlocal final_res
                final_res += left_sum + right_sum
            res = 0
            if node.left: res += node.left.val
            if node.right: res += node.right.val
            return res

        dfs(root)
        return final_res
