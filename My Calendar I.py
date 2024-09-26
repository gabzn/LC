https://leetcode.com/problems/my-calendar-i/

from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.sorted_list = SortedList()

    def book(self, start: int, end: int) -> bool:
        """   
        i = 0
                   [42  44] [46  50]
            [33  41]
        
        i = 1
        [42  44]       [46  50]
               [44  45]
        """        
        i = self.sorted_list.bisect_right((start, end))
        
        if i > 0 and self.sorted_list[i - 1][1] > start:
            return False
        if i < len(self.sorted_list) and self.sorted_list[i][0] < end:
            return False

        self.sorted_list.add((start, end))
        return True
--------------------------------------------------------------
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
