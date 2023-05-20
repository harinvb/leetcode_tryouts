from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        for i in t:
            freq[i] -= 1
        for i in freq.values():
            if i != 0: return False
        return True
