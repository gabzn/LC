https://leetcode.com/problems/moving-average-from-data-stream/
  
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.vals = deque()
        self.cur_sum = 0

    def next(self, val: int) -> float:
        self.cur_sum += val
        self.vals.append(val)
        
        if len(self.vals) > self.size:
            self.cur_sum -= self.vals.popleft()
        
        return self.cur_sum / len(self.vals)
