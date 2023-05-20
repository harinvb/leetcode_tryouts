from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        used_numbers = set()
        deletions_req = 0
        for c, f in list(Counter(s).items()):
            new_freq = f
            while new_freq > 0 and new_freq in used_numbers:
                new_freq -= 1
            deletions_req += f - new_freq
            used_numbers.add(new_freq)
        return deletions_req


print(Solution().minDeletions('aab'))
