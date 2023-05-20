from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        out_degree_arr = [0] * n
        adj_list = [[] for _ in range(n)]
        for a,b in edges:

