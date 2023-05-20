from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.nf = defaultdict(int)
        self.ff = defaultdict(int)

    def add(self, number: int) -> None:
        cur_nf = self.nf[number]
        self.nf[number] += 1
        self.ff[cur_nf] -= 1
        self.ff[cur_nf + 1] += 1
        if self.ff[cur_nf] <= 0:
            del self.ff[cur_nf]
        if self.nf[number] <= 0:
            del self.nf[number]

    def deleteOne(self, number: int) -> None:
        cur_nf = self.nf[number]
        if cur_nf > 0:
            self.nf[number] -= 1
            self.ff[cur_nf] -= 1
            self.ff[cur_nf - 1] += 1
            if self.ff[cur_nf] <= 0:
                del self.ff[cur_nf]
            if self.nf[number] <= 0:
                del self.nf[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.ff[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
