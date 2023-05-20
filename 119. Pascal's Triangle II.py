from datetime import datetime
from functools import cache
from typing import List


class Solution:
    @cache
    def getRow(self, rowIndex: int) -> List[int]:
        p, pp = [1, 1], [1]
        if rowIndex == 0: return pp
        for i in range(rowIndex):
            pp = [1]
            for j in range(1, len(p)):
                pp.append(p[j - 1] + p[j])
            pp.append(1)
            pp, p = p, pp
        return p


s = Solution()
res = []
for i in range(10):
    start_time = datetime.now()
    res = s.getRow(10000)
    end_time = datetime.now()
    print(f'{end_time - start_time} ms')
# print(res)
