https://leetcode.com/problems/logger-rate-limiter/

class Logger:
    
    def __init__(self):
        self.logger = defaultdict(int)
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger and self.logger[message] + 10 > timestamp:
            return False
            
        self.logger[message] = timestamp
        return True
