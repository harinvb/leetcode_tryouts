# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        que = deque([root])
        while que:
            curr_qsize = len(que)

            for i in range(curr_qsize):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                    que.append(curr.right)
                if i < curr_qsize - 1:
                    curr.next = que[0]

        return root
