import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple, list[str]] = collections.defaultdict(list)
        for s in strs:
            ss = tuple(sorted(s))
            groups[ss].append(s)
        return [v for _, v in groups.items()]


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
