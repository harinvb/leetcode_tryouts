from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n + 1))
        res = []

        def _combine(at: int, cur: List):
            if at >= n:
                if len(cur) == k:
                    res.append(cur[:])
                return
            _combine(at + 1, cur)
            cur.append(arr[at])
            _combine(at + 1, cur)
            cur.pop()

        _combine(0, [])
        return res


print(Solution().combine(4, 2))
