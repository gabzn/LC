https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree:

    def __init__(self):
        self.diff = defaultdict(int)
        self.max_booking = 0
        
    def book(self, start_time: int, end_time: int) -> int:
        self.diff[start_time] += 1
        self.diff[end_time] -= 1
        
        event_count = 0
        for time, count in sorted(self.diff.items()):
            event_count += count
            self.max_booking = max(self.max_booking, event_count)
        
        return self.max_booking
