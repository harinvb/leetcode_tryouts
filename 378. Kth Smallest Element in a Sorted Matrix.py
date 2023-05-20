import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = len(matrix)
        min_heap = []
        for i in range(l):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        while k > 1:
            k -= 1
            _, i, j = heapq.heappop(min_heap)
            if j + 1 < l:
                heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1))
        _, i, j = heapq.heappop(min_heap)
        return matrix[i][j]
