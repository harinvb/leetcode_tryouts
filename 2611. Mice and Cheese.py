from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        both = [(x, y) for x, y in zip(reward1, reward2)]
        both.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for i, val in enumerate(both):
            if i < k:
                ans += val[0]
            else:
                ans += val[1]
        return ans


s = Solution()
print(s.miceAndCheese(reward1=[1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2))
print(s.miceAndCheese(reward1=[1, 1], reward2=[1, 1], k=2))
