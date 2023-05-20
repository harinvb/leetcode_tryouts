from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = defaultdict(list)
        for person, size in enumerate(groupSizes):
            group_map[size].append(person)
        res = []
        for group, persons in group_map.items():
            for g in range(0, len(persons), group):
                res.append(persons[g:g + group])
        return res


print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
