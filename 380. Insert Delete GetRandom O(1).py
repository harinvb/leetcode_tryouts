import random
from typing import List


class RandomizedSet:

    def __init__(self):
        self.lst: List[int] = []
        self.index_map: dict[int, int] = dict()
        self.index = 0

    def insert(self, val: int) -> bool:
        if val in self.index_map: return False
        self.lst.append(val)
        self.index_map[val] = self.index
        self.index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map: return False
        val_idx = self.index_map[val]
        replacement = self.lst.pop()
        if val_idx != self.index - 1:
            self.lst[val_idx] = replacement
            self.index_map[replacement] = val_idx
        del self.index_map[val]
        self.index -= 1
        return True

    def getRandom(self) -> int:
        return self.lst[random.randint(0, self.index)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
