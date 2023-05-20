from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sz = len(cost)
        two_behind, one_behind = 0, cost[sz - 1]
        for i in range(sz - 2, -1, -1):
            two_behind, one_behind = one_behind, min(cost[i] + one_behind, cost[i] + two_behind)
        return min(one_behind, two_behind)


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20, 1]))
