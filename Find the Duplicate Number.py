https://leetcode.com/problems/find-the-duplicate-number/
  
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]       # Move slow 1 at a time.
            fast = nums[nums[fast]] # Move fast 2 at a time.
            
            if slow == fast:
                break
                
        ptr = 0                 # Use another ptr to find the beginning of the cycle.
        while True:
            ptr = nums[ptr]     # Move ptr 1 at a time.
            slow = nums[slow]   # Move slow 1 at a time. Slow was already trapped in the cycle.
            
            if ptr == slow:
                return ptr
