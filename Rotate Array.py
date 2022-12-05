https://leetcode.com/problems/rotate-array/
  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        if L == k or L == 1:
            return
        k = k % L
        nums.reverse()
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, L - 1)
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

#         new_num = [0] * len(nums)
#         for ind, num in enumerate(nums):
#             new_num[(ind+k) % len(nums)] = num
        
#         for ind, num in enumerate(new_num):
#             nums[ind] = num
