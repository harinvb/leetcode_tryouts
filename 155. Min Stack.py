class MinStack:
    stck: []

    def __init__(self):
        self.stck = []

    def push(self, val: int) -> None:
        if not self.stck:
            self.stck.append((val, val))
        else:
            self.stck.append((val, min(val, self.stck[-1][1])))

    def pop(self) -> None:
        self.stck.pop()

    def top(self) -> int:
        return self.stck[-1][0]

    def getMin(self) -> int:
        return self.stck[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
