from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree_arr = [0] * (numCourses + 1)
        adj_map = defaultdict(set)
        for a, b in prerequisites:
            degree_arr[a] += 1
            adj_map[b].add(a)
        q = deque()
        for i, d in enumerate(degree_arr):
            if d == 0: q.append(i)
        visited_nodes = 0
        while q:
            pre = q.pop()
            for i in adj_map[pre]:
                degree_arr[i] -= 1
                if degree_arr[i] == 0:
                    q.append(i)
            degree_arr[pre] -= 1
            visited_nodes += 1
        return True if visited_nodes == numCourses + 1 else False


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
