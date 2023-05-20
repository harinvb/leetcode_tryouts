# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_arr(arr: List[int]):
        pre = ListNode(0)
        curr = pre
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return pre.next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        pre = ListNode(0)
        pre.next = head
        tortoise = pre
        hare = pre.next
        while hare and hare.next:
            if hare == tortoise:
                return True
            hare = hare.next.next
            tortoise = tortoise.next
        return False


print(Solution().hasCycle(ListNode.from_arr([3, 2, 0, -4])))
