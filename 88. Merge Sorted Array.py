from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        while i >= 0:
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1


a = [0, 0, 0, 0, 0]
Solution().merge(nums1=a, m=0, nums2=[1, 2, 3, 4, 5], n=5)
print(a)
