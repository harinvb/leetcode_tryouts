import collections
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degree_arr = [0] * (n + 1)
        adj_map = collections.defaultdict(set)
        for pre, cur in relations:
            degree_arr[cur] += 1
            adj_map[pre].add(cur)
        q = collections.deque()
        sems = 0

        def add_to_q():
            for course, degree in enumerate(degree_arr):
                if degree == 0:
                    q.append(course)

        add_to_q()
        visited = 0
        while q:
            sems += 1
            while q:
                pre = q.pop()
                for i in adj_map[pre]:
                    degree_arr[i] -= 1
                degree_arr[pre] -= 1
                visited += 1
            add_to_q()
        return sems if visited == n + 1 else -1


s = Solution()
print(s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))
