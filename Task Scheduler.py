https://leetcode.com/problems/task-scheduler/
  
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        
        counter = collections.Counter(tasks)  
        time, max_heap = 0, []
        for _, count in counter.items():
            heappush(max_heap, -count)
        
        while max_heap:    
            # Usuaully we need to pull n + 1 tasks from the heap, but if the heap doesn't have n + 1 tasks we just pull whatever is in the heap.
            poll_times = min(n + 1, len(max_heap))
            
            freqs = []
            for ind in range(poll_times):
                # After you pop the most freq task, DO NOT put it back immediately.
                # For eaxmple, 5A3B and CD is 2, If you take out A, decrement the count and put it back. You will take out A again, but it's not allowed since CD is 2. 
                # That's why freqs exists, we need something to store them.
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
