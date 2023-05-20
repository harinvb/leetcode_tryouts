import collections
import itertools

from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = collections.defaultdict(list)
        # sorting and collecting the user visited patterns for each user
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        # to find each unique combination of user pattern and the total count of such patterns across all users
        count = sum([collections.Counter(set(itertools.combinations(dp[u], 3))) for u in dp], collections.Counter())
        # min is used to find the most repeated combination by applying
        # negation to count and lexicographically smallest as a tuple
        return list(min(count, key=lambda k: (-count[k], k)))


print(Solution().mostVisitedPattern(
    username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
    timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]))
