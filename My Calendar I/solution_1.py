class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for a, b in self.bookings:
            if self.bookings and (a <= start < b or a <= end <= b or start < a and end > b):
                return False
        
        self.bookings.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)