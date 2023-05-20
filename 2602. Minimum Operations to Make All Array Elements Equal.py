from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans, n, prefix = [], len(nums), [0] + list(accumulate(nums))
        for query in queries:
            idx = bisect_left(nums, query)
            sub_req = ((query * idx) - prefix[idx])
            add_req = (prefix[-1] - prefix[idx]) - (query * (n - idx))
            ans.append(sub_req + add_req)
        return ans


s = Solution()
print(s.minOperations(nums=[3, 1, 6, 8], queries=[1, 5]))
print(s.minOperations(nums=[2, 9, 6, 3], queries=[10]))
