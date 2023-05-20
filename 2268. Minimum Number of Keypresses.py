from collections import Counter
from math import ceil


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        n = 1
        res = 0
        for cnt in sorted(Counter(s).values()):
            res += cnt * (ceil(n / 9))
            n += 1
        return res


print(Solution().minimumKeypresses("abcdefghijkl"))
