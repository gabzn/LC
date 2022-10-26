https://leetcode.com/problems/design-an-ordered-stream/
  
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.start_returning_index = 1

        
    def insert(self, idKey: int, value: str) -> List[str]:
        index = idKey - 1
        self.stream[index] = value
        
        largest_chunk = []
        if idKey != self.start_returning_index:
            return largest_chunk
        
        while index < len(self.stream) and self.stream[index]:
            largest_chunk.append(self.stream[index])
            index += 1
        
        self.start_returning_index = index + 1
        return largest_chunk
    
    
"""
The insertion is easy. Just find the index and put the value in that index.

What's confusing is the return part.
The FIRST non-empty return value happens when the first index is inserted AKA (idKey == 1 or idKey == start_returning_index which was initialized to be 1)


Keep appending to the chunk as long as the current cell is not empty.
Once we move to an empty cell, we set start_returning_index to this cell.
When idKey == start_returning_index again, we repeat.
"""
