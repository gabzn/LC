https://leetcode.com/problems/design-hit-counter/

class HitCounter:

    def __init__(self):
        self.queue = deque()
    
    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)    

    def getHits(self, timestamp: int) -> int:
        while self.queue:
            if self.queue[0] <= timestamp - 300:
                self.queue.popleft()
            else:
                break
                
        return len(self.queue)
