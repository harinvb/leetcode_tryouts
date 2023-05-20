# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = dict()
        cur = head
        while cur:
            node_map[cur] = Node(x=cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next: node_map[cur].next = node_map[cur.next]
            if cur.random: node_map[cur].random = node_map[cur.random]
            cur = cur.next
        return node_map[head]
