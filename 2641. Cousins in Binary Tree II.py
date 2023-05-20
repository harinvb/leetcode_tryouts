# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy_parent = TreeNode(-1)
        cur_lvl = [(dummy_parent, root)]
        cur_children_sum: defaultdict[TreeNode, int] = defaultdict(int)
        cur_children_sum[dummy_parent] = 0
        cur_lvl_sum = 0
        while cur_lvl:
            next_lvl = []
            next_children_sum: defaultdict[TreeNode, int] = defaultdict(int)
            next_lvl_sum = 0
            for parent, node in cur_lvl:
                node.val = cur_lvl_sum - cur_children_sum[parent]
                if node.left:
                    next_children_sum[node] += node.left.val
                    next_lvl.append((node, node.left))
                    next_lvl_sum += node.left.val
                if node.right:
                    next_children_sum[node] += node.right.val
                    next_lvl.append((node, node.right))
                    next_lvl_sum += node.right.val
            cur_children_sum = next_children_sum
            cur_lvl = next_lvl
            cur_lvl_sum = next_lvl_sum
        return root


{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
