import time


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = map()

        def permute_backtrack(at: int, used: set[int], prev_number: int):
            if at >= n:
                return 0
            if s[at] == 'D':
                for i in range(prev_number):
                    if i not in used:
                        used.add(i)
                        permute_backtrack(at + 1, used, i)
                        used.remove(i)
            else:
                for i in range(prev_number + 1, n + 1):
                    if i not in used:
                        used.add(i)
                        permute_backtrack(at + 1, used, i)
                        used.remove(i)

        for first_pos in range(n + 1):
            permute_backtrack(0, {first_pos}, first_pos)
        return res


start = time.time()
print(Solution().numPermsDISequence("DID"))
print(f'Time taken : {time.time() - start}')
