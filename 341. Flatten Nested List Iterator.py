# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    nums = []
    ptr: int
    l: int

    def __init__(self, nestedList: [NestedInteger]):
        self.add(nestedList)
        self.l = len(self.nums)
        self.ptr = 0

    def add(self, ni: [NestedInteger]):
        for i in ni:
            if i.isInteger():
                self.nums.append(i.getInteger())
            else:
                self.add(i.getList())

    def next(self) -> int:
        self.ptr += 1
        return self.nums[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr < self.l - 1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
