# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return to_string(self)


# def to_string(node) -> str:
#     return to_string(node.left) + ' ' + str(node.val) + ' ' + to_string(node.right) if node else 'null'


def to_string(node) -> str:
    return str(node.val) + ' ' + to_string(node.left) + ' ' + to_string(node.right) if node else 'null'


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = len(inorder)
        inorder_index_map = dict((n, i) for i, n in enumerate(inorder))
        preorder_index = 0

        def build(lft: int, rgt: int):
            nonlocal preorder_index
            if lft > rgt:
                return None

            root_val = preorder[preorder_index]
            root_idx = inorder_index_map[root_val]
            root_node = TreeNode(root_val)
            preorder_index += 1
            root_node.left = build(lft, root_idx - 1)
            root_node.right = build(root_idx + 1, rgt)
            return root_node

        return build(0, l - 1)


print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
