https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)
