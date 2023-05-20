from collections import defaultdict
from typing import List


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj_map = defaultdict(set)
        for a, b in corridors:
            if a < b:
                adj_map[a].add(b)
            else:
                adj_map[b].add(a)
        cycles = 0
        for a, b in corridors:
            s_a = adj_map[a]
            s_b = adj_map[b]
            cycles += len(s_a.intersection(s_b))
        return cycles


print(Solution().numberOfPaths(n=5, corridors=[[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]))
