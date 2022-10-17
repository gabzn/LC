https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
  
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. 
For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

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
