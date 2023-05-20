from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        return 1 + sum(damage) - max_damage if armor >= max_damage else 1 + sum(damage) - armor


print(Solution().minimumHealth(damage=[2, 5, 3, 4], armor=7))
