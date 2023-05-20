# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        old_tail = head
        l = 0
        while old_tail: old_tail, l = old_tail.next, l + 1
        old_tail.next = new_tail = head
        for _ in range(l - k % l - 1): new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
