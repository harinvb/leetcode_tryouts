from heapq import heappush, heappop
from typing import List


def median_of_arr(nums):
    q, r = divmod(len(nums), 2)
    if r == 1:
        return nums[q]
    else:
        return nums[q] + nums[q + 1]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0:
            return median_of_arr(nums2)
        elif n2 == 0:
            return median_of_arr(nums1)
        hep = []
        heappush(hep, (nums1[0], 1, 0))
        heappush(hep, (nums2[0], 2, 0))
        mid, rem = divmod((n1 + n2), 2)
        while mid > 1:
            _, arr, idx = heappop(hep)
            nums = nums1 if arr == 1 else nums2
            l = n1 if arr == 1 else n2
            if idx + 1 < l:
                heappush(hep, (nums[idx + 1], arr, idx + 1))
            mid -= 1


a = bin(12)[2:]
print(int('1' * (12 - len(a)) + a, 2))
