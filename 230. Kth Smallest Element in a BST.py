from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        found = False
        res = None
        curr = k

        def dfs(node):
            if node is None or found: return
            dfs(node.left)
            nonlocal curr, res
            curr -= 1
            if curr == 0:
                res = node.val
                found = True
            dfs(node.right)

        dfs(root)
        return res


s = Solution()
print(s.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))
