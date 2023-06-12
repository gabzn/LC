https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        res = 0
        while k:
            res = -heapq.heappop(nums)
            k -= 1
        
        return res   
-------------------------------------------------------------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        heapq.heapify(nums)
        number_of_pops = len(nums) - k
        
        while number_of_pops:
            heapq.heappop(nums)
            number_of_pops -= 1
            
        return nums[0]
