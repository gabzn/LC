https://leetcode.com/problems/task-scheduler/
  
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)  
        time = 0
        
        max_heap = []
        for _, count in counter.items():
            heappush(max_heap, -count)
        
        while max_heap:    
            # poll_times tells us how many elements we need to poll from the heap
            poll_times = min(n + 1, len(max_heap))
            
            # freqs tells us all the freqs we poll from the heap
            freqs = []
            for ind in range(poll_times):
                freq = heappop(max_heap)
                freq += 1
                
                if freq:
                    freqs.append(freq)
            
            if len(freqs) > 0:
                time += n + 1
            else:
                time += poll_times
                
            for freq in freqs:
                heappush(max_heap, freq)
            
        return time
