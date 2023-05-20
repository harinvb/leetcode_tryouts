import time
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent_map = {}

        def find(node: str):
            if node not in parent_map:
                return node
            parent_map[node] = find(parent_map[node])
            return parent_map[node]

        def union(node_a: str, node_b: str):
            parent_a = find(node_a)
            parent_b = find(node_b)
            parent_map[parent_b] = parent_a

        mail_to_owner_map = {}
        for account in accounts:
            for i in range(1, len(account)):
                mail_to_owner_map[account[i]] = account[0]
                if i < len(account) - 1: union(account[i], account[i + 1])
        parent_mail_to_child_mails = defaultdict(list)
        for mail in mail_to_owner_map.keys():
            parent_mail = find(mail)
            parent_mail_to_child_mails[parent_mail].append(mail)
        # return [[mail_to_owner_map[k]] + sorted(v, reverse=True) for k, v in parent_mail_to_child_mails.items()]
        res = []
        for k, v in parent_mail_to_child_mails.items():
            res.append([mail_to_owner_map[k], *sorted(v, reverse=True)])
        return res


start = time.perf_counter()
print(Solution().accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
print(f'{time.perf_counter() - start}')
