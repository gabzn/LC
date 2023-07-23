https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = self.compute_prefix_sum(nums)
        
    def compute_prefix_sum(self, nums):
        prefix_sums = [0]
        for index in range(len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[index])
        return prefix_sums
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
------------------------------------------------------------------------------
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = self.compute_prefix_sum(nums)
        
    def compute_prefix_sum(self, nums):
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        return prefix_sums
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
-----------------------------------------------------------------------------  
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum_nums = self.build_prefix_sum_nums(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum_nums[right]
        
        return self.prefix_sum_nums[right] - self.prefix_sum_nums[left-1]

    def build_prefix_sum_nums(self, nums):
        prefix_sum_nums = [nums[0]]
        
        for num in nums[1:]:
            prefix_sum_nums.append(prefix_sum_nums[-1] + num)
                
        return prefix_sum_nums
