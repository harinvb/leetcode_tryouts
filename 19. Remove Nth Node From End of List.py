# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return head
        pre_head = ListNode(0, head)
        fast_ptr = head
        slow_ptr = pre_head
        for _ in range(0, n):
            fast_ptr = fast_ptr.next
        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return pre_head.next
