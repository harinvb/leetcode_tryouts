from typing import List


class Trie:

    def __init__(self):
        self.children: dict[str, Trie] = dict()
        self.prefix_count = 0


class Solution:

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        if len(words) == 1:
            return [len(words[0])]

        def insert(tri, s):
            curr = tri
            for i in s:
                if i not in curr.children:
                    curr.children[i] = Trie()
                curr = curr.children[i]
                curr.prefix_count += 1

        def search(tri, s):
            curr = tri
            res = 0
            for i in s:
                curr = curr.children[i]
                res += curr.prefix_count
            return res

        if len(words) == 1:
            return [len(words[0])]
        trie = Trie()
        for i in words:
            insert(trie, i)
        res = []
        for i in words:
            res.append(search(trie, i))
        return res


print(Solution().sumPrefixScores(["abc", "ab", "bc", "b"]))
