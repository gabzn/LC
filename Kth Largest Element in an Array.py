https://leetcode.com/problems/kth-largest-element-in-an-array/
  
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element. You must solve it in O(n) time complexity.

Use a min-heap to keep track of the data.

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
