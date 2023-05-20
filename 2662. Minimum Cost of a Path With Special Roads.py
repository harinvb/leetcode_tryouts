from heapq import heappush, heappop
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        dst = lambda a, b, c, d: abs(a - c) + abs(b - d)
        specialRoads += [[*start, *target, dst(*start, *target)]]
        specialRoads = [(a, b, c, d, e) for a, b, c, d, e in specialRoads if dst(a, b, c, d) >= e]
        dst_map = {tuple(start): 0}
        hep = [(0, start[0], start[1])]
        while hep:
            cost, x, y = heappop(hep)
            for a, b, c, d, e in specialRoads:
                dst_x_a = dst(x, y, a, b)
                if dst_map.get((c, d), float('inf')) > cost + dst_x_a + e:
                    dst_map[(c, d)] = cost + dst_x_a + e
                    heappush(hep, (cost + dst_x_a + e, c, d))
        return dst_map.get(tuple(target), -1)


s = Solution()
print(s.minimumCost(start=[1, 1], target=[4, 5], specialRoads=[[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]))
