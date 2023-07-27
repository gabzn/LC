https://leetcode.com/problems/rle-iterator/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = self.process_input(encoding)
        
    def process_input(self, encoding):
        encoded = deque()
        for index in range(0, len(encoding), 2):
            repetition = encoding[index]
            if not repetition:
                continue
            
            num = encoding[index + 1]
            encoded.append(repetition)
            encoded.append(num)
        return encoded
        
    def next(self, n: int) -> int:
        res = -1
        
        while self.encoding and n:
            repetition = self.encoding[0]
            
            if repetition - n < 0:
                n -= repetition
                
                self.encoding.popleft()
                self.encoding.popleft()
            else:
                repetition -= n
                n = 0
                
                if repetition:
                    self.encoding[0] = repetition
                    res = self.encoding[1]
                else:
                    res = self.encoding[1]
                    self.encoding.popleft()
                    self.encoding.popleft()
                
                break
        
        if n:
            return -1
        return res
