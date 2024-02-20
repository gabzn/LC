https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator:

    def __init__(self, compressedString: str):
        self.queue = self.initialize(compressedString)
    
    def initialize(self, string):
        queue = deque()
        
        i = 0
        while i < len(string):
            j = i + 1
            
            freq = 0
            while j < len(string) and string[j].isnumeric():
                freq *= 10
                freq += int(string[j])
                j += 1
            
            queue.append((string[i], freq))
            i = j
        
        return queue
            
    def next(self) -> str:
        if not self.hasNext():
            return " "
        
        char, freq = self.queue.popleft()
        freq -= 1
        if freq:
            self.queue.appendleft((char, freq))
        
        return char
        
    def hasNext(self) -> bool:
        return self.queue
