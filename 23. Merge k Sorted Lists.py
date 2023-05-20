# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)
        if size == 0: return None
        return self.divideAndMerge(lists, 0, size - 1)

    def divideAndMerge(self, lists: List[Optional[ListNode]], start, end) -> Optional[ListNode]:
        if start == end: return lists[start]
        mid = start + (end - start) // 2
        left = self.divideAndMerge(lists, start, mid)
        right = self.divideAndMerge(lists, mid + 1, end)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        if l is None: return r
        if r is None: return l
        if l.val <= r.val:
            l.next = self.mergeTwoLists(l.next, r)
            return l
        else:
            r.next = self.mergeTwoLists(l, r.next)
            return r
