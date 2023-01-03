https://leetcode.com/problems/kth-largest-element-in-a-stream/
  
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
