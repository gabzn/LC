https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
  
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if len(nums) == 1:
            return nums[0]
        
        nums_int = [int(num) for num in nums]
        heapq.heapify(nums_int)
        
        number_of_pops = len(nums) - k
        
        while number_of_pops:
            heapq.heappop(nums_int)
            number_of_pops -= 1
            
        return str(nums_int[0])
