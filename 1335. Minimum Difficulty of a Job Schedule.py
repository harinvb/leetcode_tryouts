from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        res = 300_000_0

        def slices(start: int, end: int, cur_list: List[List[int]], cuts_used: int, cur: int, elements_used: int):
            if cur > end:
                if cuts_used == d and elements_used == n:
                    nonlocal res
                    res = min(sum(max(a) for a in cur_list), res)
                return
            cur_list.append(jobDifficulty[start:cur + 1])
            slices(cur + 1, end, cur_list, cuts_used + 1, cur + 1, elements_used + cur - start + 1)
            cur_list.pop()
            slices(start, end, cur_list, cuts_used, cur + 1, elements_used)

        slices(0, n - 1, [], 0, 0, 0)
        return res if res != 300_000_0 else -1


print(Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4))
