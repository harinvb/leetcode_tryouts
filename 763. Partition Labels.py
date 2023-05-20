from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_seen_map = {c: i for i, c in enumerate(s)}
        ptr = -1
        res = []
        prev = 0
        while ptr < n - 1:
            ptr = last_seen_map[s[ptr + 1]]
            cur = prev
            while cur < ptr:
                ptr = max(ptr, last_seen_map[s[cur]])
                cur += 1
            res.append(ptr - prev + 1)
            prev = ptr + 1
        return res


print(Solution().partitionLabels("abcd"))
