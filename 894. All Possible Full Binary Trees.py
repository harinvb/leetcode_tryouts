# Definition for a binary tree node.
import itertools
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'({self.val} , {self.left} , {self.right})'


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
        # recursive approach
        node_tree_map: dict[int, List[TreeNode]] = dict()
        node_tree_map[0] = []
        node_tree_map[1] = [TreeNode(0)]

        def backtrack(i: int):
            if i in node_tree_map: return node_tree_map[i]
            curr = []
            for j in range(1, i, 2):
                left_trees = backtrack(j)
                right_trees = backtrack(i - 1 - j)
                for l, r in itertools.product(left_trees, right_trees):
                    curr.append(TreeNode(0, l, r))
            node_tree_map[i] = curr
            return curr

        backtrack(n)
        return node_tree_map[n]"""
        node_tree_map: List[List[Optional[TreeNode]]] = [[] for i in range(n + 1)]
        node_tree_map[0] = []
        node_tree_map[1] = [TreeNode(0)]

        for i in range(3, n + 1, 2):
            curr = []
            for j in range(1, i, 2):
                left_trees = node_tree_map[j]
                right_trees = node_tree_map[i - 1 - j]
                for l, r in itertools.product(left_trees, right_trees):
                    curr.append(TreeNode(0, l, r))
            node_tree_map[i] = curr
        return node_tree_map[n]


print(Solution().allPossibleFBT(7))
