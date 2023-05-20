from typing import List


class TimeMap:

    def __init__(self):
        self.store: dict[str, List[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    @staticmethod
    def _bs_upper(lst: List[tuple[int, str]], target: int):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < lst[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        vals = self.store[key]
        idx = self._bs_upper(vals, timestamp)
        return vals[idx - 1][1] if idx != 0 else ''
