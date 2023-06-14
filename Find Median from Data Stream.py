https://leetcode.com/problems/find-median-from-data-stream/
  
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []     
    
    def addNum(self, num: int) -> None:
        """
        if left len == right len
            if num >= min heap[0]
                push to min heap aka right
            else
                push to max heap aka left
        """
        if len(self.max_heap) == len(self.min_heap):
            if not self.max_heap and not self.min_heap:
                self.min_heap.append(num)
                return
            
            if num >= self.min_heap[0]:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
            return
          
        """
        if left len < right len
            if num <= min heap[0]
                push to max
            else
                pop the min in min heap and push it to max heap
                push num to min heap
        """    
        if len(self.max_heap) < len(self.min_heap):
            if num <= self.min_heap[0]:
                heappush(self.max_heap, -num)
            else:
                prev_min = heappop(self.min_heap)
                heappush(self.max_heap, -prev_min)
                heappush(self.min_heap, num)
            return
        """
        if left len > right len
            if num >= max heap[0]
                push to min heap
            else
                pop the max in max heap and push it to min heap
                push num to max heap 
        """
        if len(self.max_heap) > len(self.min_heap):
            if num >= -self.max_heap[0]:
                heappush(self.min_heap, num)
            else:
                prev_max = heappop(self.max_heap)
                heappush(self.min_heap, -prev_max)
                heappush(self.max_heap, -num)
        
    def findMedian(self) -> float:        
        if not self.max_heap or len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if not self.min_heap or len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0  
