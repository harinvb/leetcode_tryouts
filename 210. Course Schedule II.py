from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree_arr: List[int] = [0] * (numCourses)
        adj_list: List[List[int]] = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            degree_arr[a] += 1
            adj_list[b].append(a)
        q = deque()
        for i, d in enumerate(degree_arr):
            if d == 0: q.append(i)
        res = []
        while q:
            pre = q.pop()
            for n in adj_list[pre]:
                degree_arr[n] -= 1
                if degree_arr[n] == 0:
                    q.append(n)
            res.append(pre)
        return res if len(res) == numCourses else []


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
