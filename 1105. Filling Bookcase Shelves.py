import math
from functools import lru_cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        len_of_books = len(books)

        @lru_cache
        def place(at: int) -> int:
            if at >= len_of_books:
                return 0
            res, cur_width, max_height = math.inf, 0, 0
            for i in range(at, len_of_books):
                if books[i][0] + cur_width <= shelf_width:
                    cur_width += books[i][0]
                    max_height = max(max_height, books[i][1])
                    res = min(res, max_height + place(i + 1))
                else:
                    break
            return res

        return place(0)


print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
