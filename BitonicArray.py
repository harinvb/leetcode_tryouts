from bisect import bisect_left
from typing import List

arr = [1, 3, 5, 7, 9, 8, 6, 4, 2]


def bitonic(arr: List[int], target: int) -> int:
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[lo]:
            lo = mid
        else:
            hi = mid
    center = lo
    idx_in_left_half = bisect_left(arr, target, 0, center + 1)
    if arr[idx_in_left_half] == target:
        return idx_in_left_half
    idx_in_right_half = bisect_left(arr[center::-1], target)
    if arr[idx_in_right_half] == target:
        return idx_in_right_half
    else:
        return -1


print(bitonic(arr, 8))
