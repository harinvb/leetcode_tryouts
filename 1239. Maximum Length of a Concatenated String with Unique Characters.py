from functools import cache
from typing import List


class Solution:
    arr_state: dict[str, int]
    arr_size: int
    arr: List[str]

    def maxLength(self, arr: List[str]) -> int:
        self.arr_state = dict()
        self.arr = []
        self.to_states(arr)
        self.arr_size = len(self.arr)
        return self.backtrack(0, 0)

    @cache
    def backtrack(self, index, state: int) -> int:
        if index == self.arr_size: return 0
        max_len = 0
        # use it
        if state & self.arr_state[self.arr[index]] == 0:
            max_len = max(max_len,
                          len(self.arr[index]) + self.backtrack(index + 1, state | self.arr_state[self.arr[index]]))
        max_len = max(max_len, self.backtrack(index + 1, state))
        return max_len

    def to_states(self, ss: List[str]):
        for s in ss:
            self.to_state(s)

    def to_state(self, s):
        cs = set()
        sstate = 0
        for c in s:
            if c in cs: return
            sstate |= (1 << (ord(c) - ord('a')))
            cs.add(c)
        self.arr_state[s] = sstate
        self.arr.append(s)


print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
