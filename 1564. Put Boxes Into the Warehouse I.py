from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        res = 0
        # pre process heights
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])
        for room in reversed(warehouse):
            if res < len(boxes) and boxes[res] <= room:
                res += 1
        return res


s = Solution()
print(s.maxBoxesInWarehouse([4, 3, 4, 1], [5, 3, 3, 4, 1]))
