# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(next=head)
        prev = dummy
        curr = dummy.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        dummy.next.next = None
        return prev
