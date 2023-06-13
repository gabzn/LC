https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.max_size = k
        self.heap = []
        
        for num in nums:
            if len(self.heap) == self.max_size and num > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, num)
            
            if len(self.heap) < self.max_size:
                heappush(self.heap, num)                
                       
    def add(self, val: int) -> int:
        if not self.heap:
            self.heap.append(val)
            return val

        if len(self.heap) == self.max_size and val > self.heap[0]:    
            heappop(self.heap)
            heappush(self.heap, val)
               
        if len(self.heap) < self.max_size:
            heappush(self.heap, val)
    
        return self.heap[0]
--------------------------------------------------------------------------------------------------------------  
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        heapify(self.nums)
        self.maintain_k_elements()
        
    def add(self, val: int) -> int:
        heappush(self.nums, val)
        self.maintain_k_elements()
        
        return self.nums[0]
    
    def maintain_k_elements(self):
        while self.nums and len(self.nums) > self.k:
            heappop(self.nums)
