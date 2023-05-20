from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) < sum(gas):
            return -1  # because if the total cost is greater than total gas we can attain we cannot complete the trip
        # greedily select the station which can offer more than the cost
        start = 0
        curr_tank = 0
        for i, g in enumerate(gas):
            curr_tank += g - cost[i]
            if curr_tank < 0:
                # cannot start from prev start so empty tank and select next position as start
                curr_tank = 0
                start = i + 1
        return start
