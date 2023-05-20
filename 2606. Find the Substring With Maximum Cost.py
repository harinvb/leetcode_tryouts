from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        weights = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                   'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                   'x': 24, 'y': 25, 'z': 26}
        for c, val in zip(chars, vals):
            weights[c] = val
        cur_sum = 0
        max_sum = 0
        for c in s:
            cur_sum += weights[c]
            if cur_sum < 0:
                cur_sum = 0
            max_sum = max(max_sum, cur_sum)
        return max(max_sum, cur_sum)


s = Solution()
print(s.maximumCostSubstring(s="adaa", chars="d", vals=[-1000]))
print(s.maximumCostSubstring("abc", chars="abc", vals=[-1, -1, -1]))
print(s.maximumCostSubstring("hghhghgghh", "hg", [2, 3]))
