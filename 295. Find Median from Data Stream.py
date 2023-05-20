from bisect import bisect_left


class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.arr.append(num)
        else:
            self.arr.insert(bisect_left(self.arr, num), num)
        self.length += 1

    def findMedian(self) -> float:
        half = self.length // 2
        if self.length % 2 == 0:
            return (self.arr[half - 1] + self.arr[half]) / 2
        else:
            return self.arr[half] / 1


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
