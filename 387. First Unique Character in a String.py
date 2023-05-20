from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cntr = Counter(s)
        for i, c in enumerate(s):
            if cntr[c] == 1:
                return 1
        return -1
