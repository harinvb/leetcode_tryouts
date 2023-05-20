from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree_arr = [0] * n
        for a, b in roads:
            degree_arr[a] += 1
            degree_arr[b] += 1
        res = 0
        for d in reversed(sorted(degree_arr)):
            res += d * n
            n -= 1
        return res


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
