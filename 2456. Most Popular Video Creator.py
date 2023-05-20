from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_dict = dict()
        n = len(ids)
        max_popularity = -1
        for i in range(n):
            creator = creators[i]
            cviews = views[i]
            cid = ids[i]
            if creator not in creator_dict:
                creator_dict[creator] = [cviews, cviews, cid]
                max_popularity = max(max_popularity, cviews)
            else:
                cur = creator_dict[creator]
                if cur[1] < cviews:
                    cur[1] = cviews
                    cur[2] = cid
                elif cur[1] == cviews and cur[2] > cid:
                    cur[2] = cid
                cur[0] += cviews
                max_popularity = max(max_popularity, cur[0])
        return [[k, v[2]] for k, v in creator_dict.items() if v[0] == max_popularity]


print(Solution().mostPopularCreator(creators=["alice", "bob", "alice", "chris"], ids=["one", "two", "three", "four"],
                                    views=[5, 10, 5, 4]))
