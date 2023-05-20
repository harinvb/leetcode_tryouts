from functools import cache
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True)
        adj_map = {word: [] for word in words}
        for word in words:
            for i in range(len(word)):
                word_with_del_char = word[:i] + word[i + 1:]
                if word_with_del_char in adj_map:
                    adj_map[word].append(word_with_del_char)

        @cache
        def max_depth(cur_word: str):
            if len(adj_map[cur_word]) == 0:
                return 1
            d = 0
            for neigh in adj_map[cur_word]:
                d = max(max_depth(neigh) + 1, d)
            return d

        max_chain_length = 0
        for word in words:
            max_chain_length = max(max_chain_length, max_depth(word))
        return max_chain_length


print(Solution().longestStrChain(["abcd", "dbqca"]))
