https://leetcode.com/problems/sliding-window-maximum/
  
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        
        for idx, num in enumerate(nums):
            # Check if the leftmost index is out of boundary => idx - queue[0] >= k
            if queue and idx - queue[0] >= k:
                queue.popleft()
            
            # Keep the element in the queue decreasing. Pop everything that's less than the current num
            while queue and nums[queue[-1]] < num:
                queue.pop()
            
            # After poping all elements that are less than the current num, add the idx of current num
            queue.append(idx)
            
            # Add num to res when we've at least visited k - 1 nums
            if idx >= k - 1:
                res.append(nums[queue[0]])
        
        return res
