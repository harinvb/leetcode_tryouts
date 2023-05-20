# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def build(ar: List) -> ListNode:
    head = cur = ListNode(val=ar[0])
    for i in range(1, len(ar)):
        cur.next = ListNode(val=ar[i])
        cur = cur.next
    return head


def printls(ls: ListNode) -> None:
    while ls.next:
        print(str(ls.val) + '->', end='')
        ls = ls.next
    print(ls.val)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
            nodes[-1].next = None
        l = len(nodes)

        def reverse(nums: List, start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        grp_start = 0
        grp_size = 0
        for i in range(l):
            grp_size += 1
            if grp_size == k:
                reverse(nodes, grp_start, i)
                grp_start = i + 1
                grp_size = 0

        for i in range(l - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]


printls(Solution().reverseKGroup(build([1, 2, 3, 4, 5]), 2))
