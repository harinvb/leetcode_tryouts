# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        dummy = ListNode(-1, head)
        two = dummy.next
        one = dummy
        while two and two.next:
            temp = two.next.next
            one.next = two.next
            two.next.next = two
            two.next = temp
            one = two
            two = one.next
        return dummy.next
