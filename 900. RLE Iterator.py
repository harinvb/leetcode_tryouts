from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.ptr = 0

    def next(self, n: int) -> int:
        while self.ptr < len(self.encoding) and self.encoding[self.ptr] < n:
            n -= self.encoding[self.ptr]
            self.encoding[self.ptr] = 0
            self.ptr += 2
        if self.ptr > len(self.encoding): return -1
        self.encoding[self.ptr] -= n
        return self.encoding[self.ptr]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
