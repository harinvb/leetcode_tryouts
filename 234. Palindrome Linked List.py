# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a, b = self.getAsHalves(head)
        while a and b:
            if a.val != b.val: return False
            a = a.next
            b = b.next
        return True

    def getAsHalves(self, node: Optional[ListNode]):
        height = 0
        temp = node
        while temp:
            height += 1
            temp = temp.next
        pre = ListNode(next=node)
        first = pre
        second = node
        for _ in range(height // 2):
            second = second.next
            first = first.next
        if height % 2 == 1: second = second.next
        first.next = None
        return self.reverse(node), second

    def reverse(self, node: Optional[ListNode]):
        if not node: return node
        pre = ListNode(next=node)
        prev = pre
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        pre.next.next = None
        return prev


print(Solution().isPalindrome(ListNode(1, ListNode(2))))
