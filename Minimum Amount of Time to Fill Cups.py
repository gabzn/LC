https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
  
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0
        max_heap = [-cup for cup in amount if cup != 0]
        heapq.heapify(max_heap)
        
        while len(max_heap) >= 2:
            first_cup = heapq.heappop(max_heap)
            second_cup = heapq.heappop(max_heap)
                
            first_cup += 1
            second_cup += 1
    
            if first_cup:
                heapq.heappush(max_heap, first_cup)
            if second_cup:
                heapq.heappush(max_heap, second_cup)
            
            seconds += 1

        if max_heap:
            seconds += abs(max_heap[0])
            
        return seconds
