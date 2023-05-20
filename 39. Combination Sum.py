from collections import defaultdict
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        target_map: dict[int, set[tuple[int]]] = defaultdict(set)
        candidates.sort()
        for i in range(target + 1):
            for candidate in candidates:
                if candidate > i:
                    break
                if candidate % i == 0:
                    target_map[i].add(tuple(candidate for _ in range(i // candidate)))
                for possibility in target_map[i - candidate]:
                    cur = list(possibility)
                    cur.append(candidate)
                    cur.sort()
                    target_map[i].add(tuple(cur))
        return [list(pos) for pos in target_map[target]]


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
