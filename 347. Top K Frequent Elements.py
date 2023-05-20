import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [a[0] for a in collections.Counter(nums).most_common(k)]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
