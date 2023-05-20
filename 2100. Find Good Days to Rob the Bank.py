from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        days = len(security)
        if time == 0: return list(range(days))
        if (2 * time) + 1 > days: return []
        before = []
        res = []
        cnt = 0
        for day in range(days):
            cnt = cnt + 1 if day > 0 and security[day - 1] >= security[day] else 0
            if cnt >= time:
                before.append(day)
        cnt = 0
        for day in range(days - 1, -1, -1):
            if not before: break
            cnt = cnt + 1 if day < days - 1 and security[day] <= security[day + 1] else 0
            if cnt >= time and before[-1] == day:
                res.append(day)
            if day <= before[-1]:
                before.pop()
        return res


print(Solution().goodDaysToRobBank(security=[1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], time=2))
