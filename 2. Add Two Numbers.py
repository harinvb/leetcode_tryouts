# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(node1: Optional[ListNode], node2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if node1 and node2:
                carry, node1.val = divmod(carry + node1.val + node2.val, 10)
                node1.next = add(node1.next, node2.next, carry)
                return node1
            elif node1:
                carry, node1.val = divmod(carry + node1.val, 10)
                node1.next = add(node1.next, node2, carry)
                return node1
            elif node2:
                carry, node2.val = divmod(carry + node2.val, 10)
                node2.next = add(node1, node2.next, carry)
                return node2
            else:
                if carry:
                    return ListNode(1)

        return add(l1, l2, 0)


print('ab'[1:2])
