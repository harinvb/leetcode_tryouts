from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        imap: defaultdict[int, list] = defaultdict(list)
        for num_idx, num in enumerate(nums):
            imap[num].append(num_idx)
        for idxs in imap.values():
            parr, n = [0] + list(accumulate(idxs)), len(idxs)
            for idx, num in enumerate(idxs):
                left_sum = (num * idx) - parr[idx]
                right_sum = (parr[n] - parr[idx + 1]) - ((n - idx - 1) * num)
                nums[num] = left_sum + right_sum
        return nums


s = Solution()
print(s.distance([1, 3, 1, 1, 2]))
