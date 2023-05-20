from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        def get_diff(str1: str, str2: str) -> int:
            return sum(map(lambda a: a[0] != a[1], zip(str1, str2)))

        adj_map = defaultdict(set)
        all_words = [beginWord, *wordList]
        l = len(all_words)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if get_diff(all_words[i], all_words[j]) == 1:
                    adj_map[all_words[i]].add(all_words[j])
                    adj_map[all_words[j]].add(all_words[i])
        q = {beginWord}
        level = 1
        visited = {beginWord}
        while q:
            if endWord in visited:
                return level
            new_level = set()
            for word in q:
                for ne in adj_map[word]:
                    if ne not in visited:
                        visited.add(ne)
                        new_level.add(ne)
            q = new_level
            level += 1
        return 0


print(Solution().ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
