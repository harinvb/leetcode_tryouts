from bisect import bisect_right


class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_right(self.bookings, (-1, start)) - 1
        if len(self.bookings) or self.bookings[idx][1] <= start:
            self.bookings.insert(idx + 1, (start, end))
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
