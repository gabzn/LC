https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events.append((start, end))
            return True
        
        self.events.sort()
        for s, e in self.events:
            if not (end <= s or start >= e):
                return False
        
        self.events.append((start, end))
        return True
