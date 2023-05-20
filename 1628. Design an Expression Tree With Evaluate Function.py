from abc import ABC, abstractmethod
from typing import List, Optional

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):

    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def evaluate(self) -> int:
        return TreeNode._evaluate(self)

    @staticmethod
    def _evaluate(node: 'TreeNode') -> int:
        if node is None: return 0
        match node.val:
            case '+':
                return TreeNode._evaluate(node.lft) + TreeNode._evaluate(node.rgt)
            case '-':
                return TreeNode._evaluate(node.lft) - TreeNode._evaluate(node.rgt)
            case '*':
                return TreeNode._evaluate(node.lft) * TreeNode._evaluate(node.rgt)
            case '/':
                return TreeNode._evaluate(node.lft) // TreeNode._evaluate(node.rgt)
            case default:
                return int(default)

    def __init__(self, val: str, lft: Optional['TreeNode'] = None, rgt: Optional['TreeNode'] = None):
        self.val = val
        self.lft = lft
        self.rgt = rgt


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> Node:
        stck = []
        for e in postfix:
            if e in ('+', '-', '*', '/'):
                rgt = stck.pop()
                lft = stck.pop()
                stck.append(TreeNode(e, lft, rgt))
            else:
                stck.append(TreeNode(e))
        return stck.pop()


"""
Your TreeBuilder object will be instantiated and called as such:
"""
postfix = ["4", "5", "2", "7", "+", "-", "*"]
obj = TreeBuilder()
expTree = obj.buildTree(postfix)
ans = expTree.evaluate()
print(ans)
